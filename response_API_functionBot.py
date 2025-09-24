# importerer nødvendige biblioteker
from openai import OpenAI
import os
from dotenv import load_dotenv
import datetime
import requests
import sys
import json
print(sys.executable)
# last ned .env-filen
load_dotenv()
# hent API-nøkkelen
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# oppretter samtale historikk og rolle til chatbotten
conversationHistory = [
   {"role": "system", "content": "You are a helpful assistant."},
]
# oppretter OpenAI-klienten
client = OpenAI(api_key=OPENAI_API_KEY)
# definerer en funksjon som henter dagens dato med datetime biblioteket



# definerer verktøyene som kan brukes

tools = [
    # definerer verktøyet for å hente dagens dato
    {
        "type": "function",
        "name": "get_date",
        "description": "Get today's date.",
        "parameters": {
            "type": "object",
            "properties": {
                "sign": {
                    "type": "string",
                    "description": "get today`s date",
                },
            },
            "required": [],
        },
    },
    # definerer verktøyet for å hente vitser fra chucknorris api
    {
        "type": "function",
        "name": "get_joke",
        "description": "Get a random joke.",
        "parameters": {
            "type": "object",
            "properties": {
                "sign": {
                    "type": "string",
                    "description": "get a random joke",
                },
            },
            "required": [],
        },
    },
    # definerer verktøyet for å hente en fun fact med uselessfacts api
    {
        "type": "function",
        "name": "get_fact",
        "description": "Get a useless fact.",
        "parameters": {
            "type": "object",
            "properties": {
                "sign": {
                    "type": "string",
                    "description": "get a useless fact",
                },
            },
            "required": [],
        },
    },

]
    
# definerer funksjonen for å hente dagens dato
def get_date():
   return {"date": str(datetime.date.today())}



# definerer funksjonen for å hente vitser fra chucknorris api
def get_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    return {"joke": response.json().get("value")}



# definerer funksjonen for å hente en fun fact med uselessfacts api
def get_fact():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
    return {"fact": response.json().get("text")}



# definerer en funksjon som håndterer funksjonskall og kommunikasjon med modellen
def chat_with_gpt(user_input):
    conversationHistory.append({"role": "user", "content": user_input})
    response = client.responses.create(
        model="gpt-4.1",
        input=conversationHistory,
        tools=tools,
    )
    # returnerer svaret fra modellen
    text = getattr(response, "output_text", "")
    if text:
        conversationHistory.append({"role": "assistant", "content": text})
        return text

    # Håndterer funksjonskall
    for item in response.output:
        if item.type == "function_call":
            if item.name == "get_date": 
                date = get_date()
                conversationHistory.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps({
                        "date": date
                    })
                })
                print("Function calls are invoked")
                print (conversationHistory)


                second_response = client.responses.create(
                    model="gpt-4.1",
                    input=conversationHistory + response.output,
                    tools=tools,
                )

                text = getattr(second_response, "output_text", "")
                if text:
                    conversationHistory.append({"role": "assistant", "content": text})
                    return text
            
            elif item.name == "get_joke": 
                joke = get_joke()
                conversationHistory.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps({
                        "joke": joke
                    })
                })
                print("Function calls are invoked")
                print (conversationHistory)

                third_response = client.responses.create(
                    model="gpt-4.1",
                    input=conversationHistory + response.output,
                    tools=tools,
                )

                text = getattr(third_response, "output_text", "")
                if text:
                    conversationHistory.append({"role": "assistant", "content": text})
                    return text
            
            elif item.name == "get_fact": 
                fact = get_fact()
                conversationHistory.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps({
                        "fact": fact
                    })
                })

                print("Function calls are invoked")
                print (conversationHistory)

                fourth_response = client.responses.create(
                    model="gpt-4.1",
                    input=conversationHistory + response.output,
                    tools=tools,
                )

                text = getattr(fourth_response, "output_text", "")
                if text:
                    conversationHistory.append({"role": "assistant", "content": text})
                    return text
        else:
           # Vis ingen funksjonskall, returner det vanlige svaret
            answer = item.text.strip()
            conversationHistory.append({"role": "assistant", "content": answer})
            return answer
    
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]: 
            print("Exiting the chat. Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("chatbot:", response)
        