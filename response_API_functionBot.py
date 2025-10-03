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


conversation_ID = None


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
def chat_with_gpt():
    input_list = []  # definerer en tom liste for å legge funksjonskall resultater
    response_ID = None
    # starter en løkke for å håndtere påfølgende brukerinput og funksjonskall
    while True: 
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]: 
            print("Exiting the chat. Goodbye!")
            break

        # sender brukerinput til modellen sammen med tidligere response ID og verktøyene
        response  = client.responses.create(
            model="gpt-4.1", 
            input = user_input,
            previous_response_id=response_ID,
            tools=tools
        )
        # lagrer response ID for å kunne referere til denne i senere kall
        response_ID = response.id
        print("Chatbot:", response.output_text)

        # håndterer eventuelle funksjonskall i responsen
        while any(item.type == "function_call" for item in response.output):
            # lager en tom liste for å legge til funksjonskall resultater
            input_list = []

            # går gjennom alle elementene i responsen
            for item in response.output:
                # sjekker om elementet er et funksjonskall
                if item.type == "function_call": 
                    print(f"--> kaller funksjon: {item.name}")

                    # utfører riktig funksjon basert på funksjonskall navnet
                    if item.name == "get_date": 
                        result = get_date()
                
                    elif item.name == "get_joke": 
                        result = get_joke() 
                    
                    elif item.name == "get_fact": 
                        result = get_fact()

                    else: 
                        result = {"error": "Unknown function"}

                    # legger til funksjonskall resultatet i input_list for å sende tilbake til modellen
                    input_list.append({
                        "type": "function_call_output", 
                        "call_id": item.call_id, 
                        "output": json.dumps(result)

                    })
                    # sender funksjonskall resultatet tilbake til modellen sammen med tidligere response ID og verktøyene
                    response = client.responses.create(
                        model="gpt-4.1", 
                        input = input_list,
                        previous_response_id=response_ID,
                        tools=tools
                    )
                    # lagrer response ID for å kunne referere til denne i senere kall
                    response_ID = response.id
                    print("Chatbot:", response.output_text)
      
# Start samtalen
chat_with_gpt()
