# Section 1

## Welcome back! Time for Observability

Hey DevOps Wizards, welcome back to the battlefield! 🧙‍♂️🛠️

Hope you enjoyed your PTO and are feeling recharged because, well, I’m out the door for mine. Yep, it’s your turn to dive back into the chaos, and boy, do I have a quest for you!

While you were off sunbathing (or binge-watching your favorite show—no judgment), the Executive team had a brilliant idea. You know our beloved Doghouse webstore? The one that sometimes feels like it's held together with duct tape and prayers? Yeah, that one. Turns out, we had a few hiccups while you were sipping margaritas, and now the bigwigs have decided that what we really need is observability. And we need it yesterday.

But don't worry, they’ve chosen Datadog as the magical solution to all our woes! 

Here’s a scroll of heroic tasks that need your immediate attention:

1. First, you'll need to charm the Datadog platform and get your Sandbox Environment up and running. 
2. Make sure it actually works with our Doghouse store. I recommend starting with a ritual dance around the server rack. It might not help, but it’ll be fun.
3. Finally, sprinkle some pixie dust (or just use your scripting skills, whatever works) to ensure the observability work as intended.. Mainly looking at Metrics and Traces 👀

Remember, the fate of the Doghouse (and possibly my next PTO) rests in your capable hands. No pressure!

Good luck, and may the DevOps gods smile upon you. 🍀

## How-to

1. Add dd-trace to requirements.txt
2. Add Universal Service Tags and labels in the Docker File and make sure the app runs with ddtrace-run. 
3. Add datadog tracer to docker-compose.yaml
4. Build and run your container
5. Make sure you get traces & metrics in your Sandbox Environment

## Useful docuemntation

**Links**
[Tutorial - Enabling Tracing for a Python Application in a Container and an Agent on a Host](https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-container-agent-host/)

**Docker commands** 
```
# Build a Docker Image
docker build -t doghouse-app .

# Build your Docker Compose file
docker-compose -f docker-compose.yaml build web_app

# Launch your containers
docker-compose up web_app datadog -d
```
