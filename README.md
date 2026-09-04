# Doghouse LLM Lab

## Prerequisites

1. Install Docker Desktop, which includes Docker Compose - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Install an IDE - Example: [VSCode via Homebrew](https://formulae.brew.sh/cask/visual-studio-code) or [VSCode](https://code.visualstudio.com/)
3. Make sure you can access OpenAI-platform - [OpenAI Platform](https://platform.openai.com/)
4. Access your Datadog Sandbox Environment

## Run the application

The application uses current Flask, OpenAI Python SDK, Requests, and Datadog tracing releases. Transitive packages are resolved to their latest compatible versions during the image build.

```shell
cd doghouse-store
OPENAI_API_KEY=<your-key> docker compose up --build -d
```

Open <http://localhost:5000>. The store pages work without an OpenAI key, but the chatbot and designer require one. To stop the application, run `docker compose down` from `doghouse-store`.

To run the local smoke tests with the dependencies installed:

```shell
cd doghouse-store
python -m unittest discover -s tests -v
```

## Project layout

```
.
├── doghouse-store/       # Flask application and container configuration
├── Section1/             # OpenAI integration exercise
├── Section2/             # Agentless LLM Observability exercise
├── Section3/             # Datadog Agent exercise
├── Section4/             # Manual LLM span exercise
└── Solution/
```

## Lab instructions

1. Clone or download this repository.
2. Get your Datadog Sandbox environment ready. (If you are using .EU, you will have to specify this through out the exercise.)
   - Generate/Copy and save an API Key to use during the exercise
3. Move on to Section 1.
