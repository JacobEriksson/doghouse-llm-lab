# Section 1

## Welcome back! Time for Observability

Hey DevOps Engineer and welcome back from your PTO! 
I'm now off so I'm giving you some instructions of what needs to be done as your highest priority!

You know the Doghouse webstore, while you were gone the Executive decided that we need to implement observability.. quickly..
We had some issues when you were off.. A decision has been made to go with Datadog. 

I'v gathered a list of the things you have to accomplish:
1. Add dd-trace to requirements.txt
2. Add env, service & version-tags and labels in the Docker File together make sure the app runs with ddtrace-run. 
3. Add datadog tracer to docker-compose.yaml
4. Build and run your container
5. Make sure you get traces & metrics in your Sandbox Environment

## How-to

text