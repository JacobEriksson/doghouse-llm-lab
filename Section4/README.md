# Section 4

## Plot Twist: Just When You Thought It Was Over… 🎨✨

Tracing spans with Decorators & Annotations

#### Here's the actions:
1. Download the additional files in this folder and replace the ones in your working repository. This introduces the new Designer Application!
2. Rebuild your images and compose files and run it. 
3. Identify the different steps that's being taken in the Designer App and map those to Span types
4. Decorate the different steps so Datadog LLM Obs can identify and visualise each span individually. See Picture below for reference.
5. Regroup with the wider team and discuss the differences and outcome.

## Useful documentation

**Reference Picture**
![LLM Trace Spans](https://datadog-docs.imgix.net/images/llm_observability/llm-observability-agent-trace.d90aaafac7a89ad70cbe9caab393841f.png?fit=max&auto=format&w=1754&h=968)

**Links**
[Datadog Annottating spans](https://docs.datadoghq.com/llm_observability/setup/?tab=decorators#annotating-spans)
[Tracing LLM Spans](https://docs.datadoghq.com/llm_observability/setup/sdk/#tracing-spans)

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
