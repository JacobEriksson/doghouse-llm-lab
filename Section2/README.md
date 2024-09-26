# Section 2

## And the plot thickens, Wizards! 🧙‍♀️📈

Agentless LLM Obs & deploy designer

## Exercise
1. Update the docker-compose.yaml with necessary environment variables. See useful links!
2. Rebuild your docker compose and run and declare your variables at runtime or with a specific env file.
3. Download the files in this folder and replace the files in your library. This introduces the new Designer Application!
4. Rebuild your images and compose files and run it. 
5. Regroup with the wider team and discuss the differences with OpenAI integration and the agentless OpenAI Integration.

## Useful documentation

**Links**

- [Open AI Quickstart Guide](https://docs.datadoghq.com/llm_observability/quickstart/)
- [OpenAI Getting Started](https://platform.openai.com/docs/guides/chat-completions/getting-started)
- [Tutorial - Enabling Tracing for a Python Application in a Container and an Agent on a Host](https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-container-agent-host/)

**Docker commands** 
```
# Build a Docker Image
docker build -t doghouse-app .

# Build your Docker Compose file
docker-compose -f docker-compose.yaml build web_app

# Launch your containers
docker-compose up web_app -d
```

PS. Remember variables KEY="VALUE" docker-compose up web_app -d 

