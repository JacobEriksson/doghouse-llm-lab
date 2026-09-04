from flask import jsonify
from openai import OpenAI


def get_openai_client():
    """Create the client only when an OpenAI-backed feature is used."""
    return OpenAI()


def call_openai_tool(model, messages):
    response = get_openai_client().chat.completions.create(
        model=model,
        messages=messages,
    )
    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("OpenAI returned an empty chatbot response")
    return content.strip()

def process_user_message(user_message):
    system_message = {"role": "system", "content": "You are a forthcoming support agent working for a company called Doghouse."}
    user_input = {"role": "user", "content": user_message}
    bot_response = call_openai_tool("gpt-4o-mini", [system_message, user_input])


    return bot_response

def doghouse_chat_workflow(user_message):
    bot_response = process_user_message(user_message)
    return bot_response

def chat_handler(request):
    payload = request.get_json(silent=True) or {}
    user_message = payload.get('message')
    if not isinstance(user_message, str) or not user_message.strip():
        return jsonify(error='A non-empty message is required.'), 400
    bot_response = doghouse_chat_workflow(user_message.strip())
    return jsonify(response=bot_response)
