# Section 2 - Solution

## Create an OpenAI Organization API KEY 
See useful link, and create your API KEY and save it somewhere safe


## Create the chatbot.html and add a link in base.html page. (see Template folder) 
Copy the chatbot.html from the templates folder on github and add it to your templates folder.
Replace your templates/base.html file with the one from the github templates folder with.

## Add additional app.routes to the Flask App.

Add the following piece of code to your app.py. This will add the necessary render and link functionality to your doghouse application.
```
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')
```

## Add the OpenAI Chatbot functionality to the Flask App.
See useful links for OpenAI Documentaiton.

First we need to import and intialise OpenAI in our app.py. OpenAI() will look for :

```
#Import the following libraries
from flask import Flask, render_template, request, url_for, jsonify, redirect
import os
from openai import OpenAI

# Initialise OpenAI
client = OpenAI()
```

Secondly we have to add an app.route to make an API POST call to OpenAI:

```
@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    # Call OpenAI GPT to respond to chat
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a forth comming support agent who's working for a company called Doghouse. "},
            {"role": "user", "content": user_message}]
                )
 
    bot_response = response.choices[0].message.content.strip()

    return jsonify(response=bot_response)
```

## Add OpenAI Env variables to docker-compose file.

In the docker-compose.yaml file, add the following under your web_app:

````
services:
  web_app:
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY} #Env Variable - Set Manually at runtime
````
The app will require you to add an OPENAI_API_KEY at runtime to be able to run. 

## Add Observability

Use the provided documentaiton and give it a try.. 

Hints:
- Environment variables in docker-comopose.yaml
