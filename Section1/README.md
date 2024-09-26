# Section 1

## Welcome back! Time for Observability

OpenAI Integration

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
