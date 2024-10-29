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
2. Remove the agentless environment variable. 
3. Rebuild your images and compose files and run it. 
4. Generate some traffic using the webapp and Chatbot.
5. Regroup with the wider team and discuss the differences. 

## Useful documentation

**Links**
- [LLM Observability Quickstart](https://docs.datadoghq.com/llm_observability/quickstart/?site=us)
- [Tutorial - Enabling Tracing for a Python Application and Datadog Agent in Containers](https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-containers/)


**Docker commands** 
```
# Build your Docker Compose file
docker-compose -f docker-compose.yaml build web_app

# Launch your containers
docker-compose up web_app datadog -d
```

PS. Remember variables KEY="VALUE" docker-compose up web_app -d 

## Help

### 1. Adding the Agent to run parallel to the application
In previous section, we leveraged the agentless version of LLM Obs that gives us limited visibility in to our application. By adding the Datadog Agent, we can also start collecting additional data such as Infrastructure metrics, processes, Logs, APM and more. This also enables us to manually trace the LLM application to provide more granular insights, but more on that later.

The way to do this, we will have to update the docker-compose.yaml file and add the necessary config:

```
services:
  datadog:
    container_name: dd-agent
    image: "gcr.io/datadoghq/agent:latest"
    environment:
      - DD_APM_NON_LOCAL_TRAFFIC=true
      - DD_DOGSTATSD_NON_LOCAL_TRAFFIC="true" 
      - DD_HOSTNAME=datadog
      - DD_APM_ENABLED=true
      - DD_API_KEY=<DD_API_KEY> # Your Datadog Sandbox API Key
      # - DD_SITE=<DD_SITE> # Specify the Datadog Site where your Sandbox Environment resides

    volumes:
      - /proc/:/host/proc/:ro
      - /sys/fs/cgroup/:/host/sys/fs/cgroup:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
  web_app:
   ...
     ..
```

### 2. No more agentless
Now when we are running the application with an agent, we can remove the environment variable on the web_app that instruct the application to leverage the agent instead.

Remove the following line in your docker-compose.yaml:
```
DD_LLMOBS_AGENTLESS_ENABLED=1
```

Now launch your application:
```
docker-compose up web_app datadog -d
```