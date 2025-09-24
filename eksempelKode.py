from openai import OpenAI
import json
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

# 1. Define a list of callable tools for the model
tools = [
    {
        "type": "function",
        "name": "get_horoscope",
        "description": "Get today's horoscope for an astrological sign.",
        "parameters": {
            "type": "object",
            "properties": {
                "sign": {
                    "type": "string",
                    "description": "An astrological sign like Taurus or Aquarius",
                },
            },
            "required": ["sign"],
        },
    },
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
]

def get_horoscope(sign):
    return f"{sign}: Next Tuesday you will befriend a baby otter."


def get_date(): 
    return str(datetime.date.today())

# Create a running input list we will add to over time
input_list = [
    {"role": "user", "content": "Jeg er Skorpion. Hva er min horoskop for i dag?"},
]

# 2. Prompt the model with tools defined
response = client.responses.create(
    model="gpt-5",
    tools=tools,
    input=input_list,
)

# Save function call outputs for subsequent requests
input_list += response.output

for item in response.output:
    if item.type == "function_call":
        if item.name == "get_horoscope":
            # 3. Execute the function logic for get_horoscope
            horoscope = get_horoscope(json.loads(item.arguments))
            
            # 4. Provide function call results to the model
            input_list.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": json.dumps({
                "horoscope": horoscope
                })
            })

        if item.name == "get_date": 
            date = get_date()

            input_list.append({
                "type":  "function_call_output", 
                "call_id": item.call_id, 
                "output": json.dumps({
                "date": date
                })
            })


print("Final input:")
print(input_list)




response = client.responses.create(
    model="gpt-5",
    instructions="respond with proper function calls.",
    tools=tools,
    input=input_list,
)

# 5. The model should be able to give a response!
print("Final output:")
print(response.model_dump_json(indent=2))
print("\n" + response.output_text)