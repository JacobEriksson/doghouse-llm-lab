from flask import jsonify
from openai import OpenAI


client = OpenAI()

def call_openai_tool(model, messages):
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content.strip()

def process_user_message(user_message):
    system_message = {"role": "system", "content": "You are a forthcoming support agent working for a company called Doghouse."}
    user_input = {"role": "user", "content": user_message}
    bot_response = call_openai_tool("gpt-3.5-turbo", [system_message, user_input])


    return bot_response

def doghouse_chat_workflow(user_message):
    bot_response = process_user_message(user_message)
    return bot_response

def chat_handler(request):
    user_message = request.json.get('message')
    bot_response = doghouse_chat_workflow(user_message)
    return jsonify(response=bot_response)
