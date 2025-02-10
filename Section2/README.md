# Section 2

## And guess what? There’s more! 🧙‍♀️📈

You thought we were done? Not a chance! The execs have decided that tracking token usage isn’t enough. Oh no, they want more data—better data. Now, they want us to track performance and get visibility into the actual AI prompts being used. 

Here’s what we need to pull off:

- Monitor Performance – We’re already tracking basic usage, but now we need to dive deeper. No more vague "slowdowns"; we need specifics. When things start to crawl, we want to know why. If the chatbot’s lagging, we need to pinpoint it like a detective on a coffee bender.
- Get Visibility into Prompts – The execs want to see what the chatbot’s saying and why. They’re all about “transparency” now. We need a way to track the actual prompts being sent to OpenAI, and we need to do it without installing any extra agents. We’re looking for some sleek, behind-the-scenes magic here.

So, yeah, it's a little like pulling a rabbit out of a hat, but hey—no pressure! Let’s make this observability expansion happen, get the chatbot performing like an Olympic athlete, and give the execs the AI prompt insights they’re dreaming of.

Game on! 🏆🐾

## Exercise

1. Update the docker-compose.yaml with necessary environment variables to support agentless LLM Observability. See useful links!
2. Make sure the application run with dd-tracer in the Dockerfile. No need to install through pip as it's already in the requirements.txt
3. Rebuild your docker files and run and declare your variables at runtime or with a specific env file.
4. Test your application and see if you get any traces in LLM Observability.
5. Regroup with the wider team and discuss the differences with OpenAI integration and the agentless OpenAI Integration.

## Useful documentation

**Links**

- [Datadog LLM Observability starting guide](https://docs.datadoghq.com/llm_observability/quickstart/)
- [OpenAI Getting Started](https://platform.openai.com/docs/guides/chat-completions/getting-started)
- [Tutorial - Enabling Tracing for a Python Application and Datadog Agent in Containers](https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-containers/)

**Docker commands** 

```
# Build your Docker Compose file
docker-compose -f docker-compose.yaml build web_app

# Launch your containers
docker-compose up -d
```

PS. Remember variables KEY="VALUE" docker-compose up -d 

## Help

### 1. Docker Copmose & Variables
To be able to get started with LLM Observability we will have to make sure to prepare the Docker Compose file so all the necessary environment variables are declared. The Datadog documentation gives the following example:
```
DD_LLMOBS_ENABLED=1 DD_LLMOBS_ML_APP=onboarding-quickstart \
DD_API_KEY=<YOUR_DATADOG_API_KEY> DD_SITE=datadoghq.com \
DD_LLMOBS_AGENTLESS_ENABLED=1
```

To enable this in our app, add the following to the docker-compose.yaml file under the web-app environment section:
```
web_app:
  ...
  environment:
  - DD_LLMOBS_ENABLED=1
  - DD_LLMOBS_AGENTLESS_ENABLED=1 
  - DD_LLMOBS_ML_APP=<SERVICE NAME> # Your LLM Obs Service Name
  - DD_API_KEY=<DD_API_KEY> # Your Datadog Sandbox API Key
  - DD_SITE=datadoghq.com # Specify the Datadog Site where your Sandbox Environment resides
  ```

### 2. Run the application with dd-tracer.
In it's current shape, the container runs the web application normaly using the normal python process. We will need to update the Dockerfile or docker-compose file to run the application with the dd-tracer.

Change the Dockerfile accordingly:
```
CMD ["python", "-m", "app"]

to

CMD ["ddtrace-run", "python", "-m", "app"]
```

### 3. Rebuild your application
We will now have to rebuild your application to make sure our changes are incorporated. 

Run:
```
docker-compose -f docker-compose.yaml build web_app
```
