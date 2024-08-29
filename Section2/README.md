# Section 2

## But wait, there's more!

Turns out, observability wasn’t the only thing on the execs' wish list. Apparently, our customers have been a bit, shall we say, disgruntled with our customer support. (Who knew “Did you try turning it off and on again?” wouldn’t be the magic cure for all woes?) So, the execs have decided to jump on the latest tech bandwagon and—wait for it—implement a support bot using OpenAI. Yep, we’re officially welcoming our robot overlords to the team! 🤖

I know what you’re thinking: First observability, now this? But hey, if we’re going to be replaced by AI, we might as well enjoy the ride, right? Who knows, maybe the bots will do such a good job that we can all take extended PTO. 🌴

Here’s what you’ll need to tackle next:
1. Build the Bot - Your mission, should you choose to accept it (and trust me, you don’t have a choice), is to integrate OpenAI into our doghouse app. The goal? Make this bot so helpful that customers start asking it for life advice.

2. Keep an Eye on the Bots - But here’s the kicker: while our shiny new support bot is chatting away with customers, we need to make sure it’s not burning through our budget faster than a developer at an all-you-can-eat snack bar. We need to monitor OpenAI usage and costs—yes, with Datadog again. Think of it as giving Datadog a new hobby.

3. Ensure Smooth Integration - And of course, because nothing is ever simple, make sure this whole setup doesn’t bring down the entire Doghouse in the process. If the bot starts giving out wrong answers or setting things on fire, you’ll be the one who gets the call—probably while you’re trying to enjoy a quiet evening with a glass of wine.

So buckle up, DevOps heroes. We’re on a wild ride into the future of AI, observability, and, possibly, world domination. Let’s make sure we’re the ones in control—at least for now. 🚀

Good luck again!

## Exercise
1. Create an OpenAI Organization API KEY 
2. Create the chatbot.html and add a link in base.html page. (see Template folder) 
3. Add additional app.routes to the Flask App.
4. Add the OpenAI Chatbot functionality to the Flask App.
5. Add OpenAI Env variables to docker-compose file.
6. Build and Run your container and test the chatbot!
7. Add Observability
8. Verify

## Useful documentation

**Links**

- [OpenAI Platform & Organization overview](https://platform.openai.com/organization/api-keys)
- [OpenAI Getting Started](https://platform.openai.com/docs/guides/chat-completions/getting-started)
- [Tutorial - Enabling Tracing for a Python Application in a Container and an Agent on a Host](https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-container-agent-host/)
- [LLM Observability Quickstart](https://docs.datadoghq.com/llm_observability/quickstart/?site=us)

**Docker commands** 
```
# Build a Docker Image
docker build -t doghouse-app .

# Build your Docker Compose file
docker-compose -f docker-compose.yaml build web_app

# Launch your containers
docker-compose up web_app datadog -d
```

PS. Remember the DD_API_KEY? Now you need to add your OPENAI_API_KEY as well.


#### Conclusion

Did you manage to get it to work? 
(Topics to discuss with your collague)
- What can we see in Datadog? Dashboards, traces, metrics, LLMs?
- LLM Observability, what can we see? Anything missing?


