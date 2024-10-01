# Section 3

## Agents for life! 🎢✨

Remember how the execs were all about “no agents” last week? Well, apparently someone gave them a very convincing PowerPoint, and now they’ve done a complete 180. Turns out, adding an agent is the new “must-have” because, according to the latest wisdom, it will unlock even more “valuable data”—their words, not mine.

So, you know what that means: it’s time to switch gears and add that agent we weren’t supposed to need!

Here’s what we’re fixing up:

- Deploy the Tracing agent – The execs are convinced it’s going to give us all kinds of glorious insights into our app’s performance and AI magic. Let’s get it installed and plugged in so they can start seeing those “valuable” metrics they’re after.

- Supercharge Observability – Now that we’re agent-enabled, we can get way more detailed data. Performance metrics? Traces? Weird spikes at 3 a.m. because the chatbot decided to overthink a customer’s request for a blue doghouse? We’re going to know everything. It’s basically our new superpower.

- Impress the Execs – Let’s be real: the goal here is to make the dashboards so shiny that the execs think we’ve somehow unlocked the secrets of the universe. If the data’s looking good and the app’s running smooth, we’re golden.

So, it’s time to embrace the agent life, plug it all in, and let’s make sure that chatbot—and the rest of the system—is performing like a rock star. And who knows? Maybe this agent really will give us some next-level insights. 🚀

## Exercise

1. Add the dd-agent to docker-compose.yaml to run it in parallel to the webapp, remember to add or edit necessary environment variables. 
2. Rebuild your images and compose files and run it. 
3. Regroup with the wider team and discuss the differences. 

## Useful documentation

**Links**
- [LLM Observability Quickstart](https://docs.datadoghq.com/llm_observability/quickstart/?site=us)
- [Tutorial - Enabling Tracing for a Python Application and Datadog Agent in Containers](https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-containers/)


**Docker commands** 
```
# Build a Docker Image
docker build -t doghouse-app .

# Build your Docker Compose file
docker-compose -f docker-compose.yaml build web_app

# Launch your containers
docker-compose up web_app datadog -d
```

PS. Remember variables KEY="VALUE" docker-compose up web_app -d 
