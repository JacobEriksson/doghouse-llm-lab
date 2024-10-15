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
4. Regroup with the wider team and discuss the differences with OpenAI integration and the agentless OpenAI Integration.

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
docker-compose up web_app -d
```

PS. Remember variables KEY="VALUE" docker-compose up web_app -d 

