# importerer nødvendige biblioteker
from openai import OpenAI
import os
from dotenv import load_dotenv
import datetime
import requests
import sys
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
   {
       "type": "function",
       "function": {
           "name": "get_date",
           "description": "Returnerer dagens dato"
       }
   }
]
# definerer funksjonen for å hente dagens dato
def get_date():
   return {"date": str(datetime.date.today())}


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_joke",
            "description": "Returnerer en vits"
        }
    }
]

def get_joke():
    category = requests.get("https://api.chucknorris.io/jokes/random")
    return {category}

# definerer funksjonen for å chatte med GPT
def chat_with_gpt(prompt):
    # legger til brukerens melding i samtalehistorikken
    conversationHistory.append({"role": "user", "content": prompt})
    # sender forespørselen til OpenAI API
    response = client.chat.completions.create(
       # definerer modellen
        model="gpt-4.1",
        # legger til samtalehistorikken
        messages=conversationHistory, 
        tools=tools, 
    )
    print (response)
    # henter meldingen fra svaret
    message = response.choices[0].message

    # sjekker om det er noen verktøyanrop
    if message.tool_calls:
        for tool_call in message.tool_calls:
            if tool_call.function.name == "get_date":
                result = get_date()
                
                # legger til verktøyets svar i samtalehistorikken
                second_response = client.chat.completions.create(
                    model="gpt-4.1", 
                    messages=conversationHistory + [
                        message, 
                        {"role": "tool", "tool_call_id": tool_call.id, "content": str(result)},
                    ]
                )
                print(second_response)
                # henter svaret fra verktøyet 
                final_answer = second_response.choices[0].message.content.strip()
                conversationHistory.append({"role": "assistant", "content": final_answer})
                return final_answer
            
        if message.tool_calls:
            for tool_call in message.tool_calls:
                if tool_call.function.name == "get_joke".lower():
                    result = get_joke()
                    # legger til verktøyets svar i samtalehistorikken
                    third_response = client.chat.completions.create(
                        model="gpt-4.1", 
                        messages=conversationHistory + [
                            message,
                            {"role": "tool", "tool_call_id": tool_call.id, "content": str(result)},
                    ]
                )
                print(third_response)
                # henter svaret fra verktøyet
                final_answer = third_response.choices[0].message.content.strip()
                conversationHistory.append({"role": "assistant", "content": final_answer})
                return final_answer
    else:
        # Hvis ingen tool_calls, returner det vanlige svaret
        answer = message.content.strip() 
        conversationHistory.append({"role": "assistant", "content": answer})
        return answer

# en if setning med en while løkke som kjører samtale loopen
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chat_with_gpt(user_input)  
        print("Chatbot:", response)
        