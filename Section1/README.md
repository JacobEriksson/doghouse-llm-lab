# Section 1

## Welcome back! Time for Observability

Hey DevOps Wizards, welcome back to the battlefield! 🧙‍♂️🛠️

Hope you enjoyed your well-deserved break, because now it’s my turn to disappear into the land of relaxation. But before I vanish, I’ve got some magical tasks for you to tackle as your highest priority!

So, remember our beloved Doghouse webstore? While you were off sipping piña coladas (or whatever your vacation drink of choice is), the leadership decided it’s time to boost sales with some fancy new functionality. Their big idea? A concept designer where customers can input a few details, and voilà—we offer them the perfect doghouse to buy right on the spot. Genius, right? (And by "genius," I mean, "We’ve got our work cut out for us.")

We’ve already wrangled a company to develop the app for us—because nothing says “we’re serious” like outsourcing the hard part! Now, it’s up to you to weave your DevOps magic and get this thing up and running. Fun, right? 😅

Oh, and did I mention? While you were away, the decision was made to sprinkle some observability into the mix. Because nothing says “smooth launch” like tracking every little hiccup! So, we’ll need to keep an eye on this shiny new OpenAI app too.

Here’s what’s on your to-do list:

1. Add the HTML Files and Routes - First up, integrate those shiny new HTML files and app.routes into our Doghouse application. Make sure everything’s as smooth as a golden retriever’s coat.

2. Make sure to integrate with OpenAI - Next, make sure the application taps into our newly created OpenAI keys. We want this AI-powered doghouse ceoncept designer to be as smart as it sounds—or at least not embarrassingly dumb.

3. Instrument with Observability - And finally, let’s not forget our new favorite thing: observability! Instrument the OpenAI app with the observability Datadog thingy so we can monitor, measure, and maybe even marvel at how everything is working.

So, roll up your sleeves, grab your wand—or keyboard—and let’s make some magic happen! 🔮

## Exercise

1. Implement the designer page to our webstore (see instructions provided)
2. Leverage the OpenAI Quickstart guide to use the agentless integration
3. Update Docker-compose and Docker files
4. Build & Run the app
5. Conclusion discussion with the wider team

![Let's go teamwork](https://teamhood.com/wp-content/uploads/2022/09/teamwork-anchor-meme.jpg)


## Useful documentation

**Links**

[Datadog OpenAI Quickstart](https://docs.datadoghq.com/llm_observability/quickstart/)

**Docker commands** 
```
# Build a Docker Image
docker build -t doghouse-app .

# Build your Docker Compose file
docker-compose -f docker-compose.yaml build web_app

# Launch your containers
docker-compose up web_app datadog -d
```
PS. Don't forget to use your DD_API_KEY & OPENAI_API_KEY
