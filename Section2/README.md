# Section 2

## And the plot thickens, Wizards! 🧙‍♀️📈

Just when you thought the adventure was all about shiny new features, the execs have another task for you. You see, while you were off recharging your magical powers, our trusty Doghouse webstore encountered a few glitches. Naturally, the bigwigs decided that we need to keep a closer eye on things—because what’s better than fixing problems? Catching them before they explode!

So, we’re diving deep into the mystical arts of observability. That’s right, it’s time to add an observability agent to our app and start collecting all those sweet, sweet metrics and traces. Think of it like adding a crystal ball that lets us see everything our app is up to—only with more dashboards and less fog.

Here’s what you need to conjure up:

1. Deploy the Observability Agent - First, install and configure the observability agent within the Doghouse app. It’s like giving our app a little helper that reports back on everything it sees. (No pressure, little agent, but we’re counting on you.)

2. Collect Metrics and Traces - Next, we need to set up the collection of metrics and traces. We’re talking about everything from response times to error rates—basically, if the app blinks, we want to know about it. And if it sneezes? We need a full report.

3. Integrate with Existing Tools - Finally, tie everything into our existing observability stack. We need to make sure that the data flows seamlessly to our dashboards, where we can gaze upon it and pretend we totally understand what’s going on at all times. 📊

So, grab your cauldron—or maybe just your favorite IDE—and let’s brew up some top-notch observability. With these spells in place, we’ll have our app under a watchful eye, and you can rest easy knowing we’re catching issues before they catch us.

Good luck, and may your logs be plentiful and your metrics crystal clear! 🔍

## Exercise
1. 
2. 
3. 
4. 
5. 

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


