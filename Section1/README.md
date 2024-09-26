# Section 1

## Hey DevOps Wizards, welcome back from your PTO! 🏖️🐾

I hope you soaked up enough sunshine because things have been moving while you were gone! Remember the Doghouse webstore? Well, this summer, we introduced that shiny new chatbot (because, of course, we did), and now we need to make sure it’s not secretly running wild with OpenAI tokens and slowing things down.

Here’s what needs to happen:

- Connect to the New Observability Tool – Plug in the shiny new observability tool and make sure it’s working its magic. 
- Track Token Usage – The chatbot’s been busy, and we need to know how many OpenAI tokens it’s using. Are we on budget, or is this bot ready to bankrupt us? Time to find out!
- Monitor Usage & Requests – Keep an eye on the chatbot’s basic performance. Anything helps! 


Let’s get this sorted, make the execs happy, and ensure that chatbot doesn’t cause any chaos behind the scenes. You’ve got this! 💪✨

## Exercise

1. Build & run the doghouse application - Did it work? If not, why? Check log output in Docker if necessary.
    - App will be running on: http://localhost:5000
2. Test the chatbot to see if it works.
3. Log in to your Datadog Sandbox Environment
4. Leverage Datadog OpenAPI Integration to connect to your project and organisation.
5. Run a few prompts and see the results in your Datadog Sandbox. Do you see any usage?
6. Conclusion discussion with the wider team

![Let's go teamwork](https://teamhood.com/wp-content/uploads/2022/09/teamwork-anchor-meme.jpg)


## Useful documentation

**Links**

- [Datadog OpenAI Integration](https://docs.datadoghq.com/integrations/openai/?tab=apikey)
- [OpenAI Platform](https://platform.openai.com/)
- [OpenAI Org & API](https://platform.openai.com/organization/api-keys)

**Useful Docker commands** 
```
# Build a Docker Image
docker build -t doghouse-app .

# Build your Docker Compose file
docker-compose -f docker-compose.yaml build web_app

# Launch your containers
docker-compose up web_app -d
```
PS. Don't forget to use your OPENAI_API_KEY
