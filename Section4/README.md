# Section 4

## And now, for the grand finale… introducing the Design Studio! 🎨🐕

Yep, the execs are on fire with ideas, and this one’s actually pretty cool. We’re rolling out a Doghouse Design Studio where customers can create their dream doghouses! Custom colors, styles, sizes—the whole shebang.

The files are locked and loaded, so your job is simple (ish): download, install, and—here’s the fun part—replicate everything we did for the chatbot, but now for the design app. Only this time, it’s a bit more advanced. Because, of course it is. 😅

Here’s the game plan:

- Install the Design App – The files are ready and waiting. Just download and set it up. This should be straightforward enough. You’ve done this a million times, right? 🎯

- Replicate Observability – Now, replicate the same observability magic we did before for the chatbot. Performance monitoring, and all that good stuff. But here’s the kicker: this app is more complex, so it’ll need extra attention.

- Decorate & Annotate Spans – This is where we level up. Make sure every span is clearly annotated and decorated, so we can trace what’s happening at a glance. Whether a customer is picking out the roof color or tweaking the size, we need to see exactly what’s going on in the backend—no guessing games.

With the Design Studio, the stakes are higher and the system’s a bit more intricate, so let’s make sure we’re keeping everything organized, visible, and ready to impress. If all goes well, the execs will be patting themselves on the back for this genius move, and we’ll be sitting pretty with a fully observant, high-performing design app.

Let’s make it happen! 💥💻🐾

## Exercise

1. Time to introduce the Designer app! Run the application and test the designer page.
2. Manually trace spans using decorators and annotations to visualise each span in LLM Observability. 
    - Analyse the doghouse/designer.py file and identify the different steps and map those to LLM Span types. See useful links for more info!
3. Import the neessary libraries (dd-trace etc)
4. Decorate the different steps so Datadog LLM Obs can identify and visualise each span individually. See Picture below for reference. 
**PS. You can test it out with the chatbot first if you want to test a simpler use-case.**
5. Regroup with the wider team and discuss the differences and outcome.


**Take some Notes of the following:**
- What was the instructions / system prompt for building the doghouse suggestion?
- Do we see all the OpenAI Requests? Why?


## Useful documentation

**Reference Picture**
![LLM Trace Spans](https://datadog-docs.imgix.net/images/llm_observability/llm-observability-agent-trace.d90aaafac7a89ad70cbe9caab393841f.png?fit=max&auto=format&w=1754&h=968)

**Links**
- [LLM Observability Python SDK](https://docs.datadoghq.com/llm_observability/setup/sdk/)
- [LLM Observability Terms and Concepts including Span Types](https://docs.datadoghq.com/llm_observability/terms/)
- [Tracing LLM Spans](https://docs.datadoghq.com/llm_observability/setup/sdk/#tracing-spans)
- [Datadog Set up LLM Observability](https://docs.datadoghq.com/llm_observability/setup/?tab=decorators)
- [Datadog Annotating spans](https://docs.datadoghq.com/llm_observability/setup/?tab=decorators#annotating-spans)


**Docker commands** 
```
# Build your Docker Compose file
docker-compose -f docker-compose.yaml build web_app

# Launch your containers
docker-compose up web_app datadog -d
```

PS. Remember variables KEY="VALUE" docker-compose up web_app datadog -d 
