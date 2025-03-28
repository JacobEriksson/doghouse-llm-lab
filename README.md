# Doghouse LLM Lab

### Prereqs

1. Install Docker & Docker Compose - [Docker via Homebrew](https://formulae.brew.sh/formula/docker) & [Docker Compose via Homebrew](https://formulae.brew.sh/formula/docker-compose) or [Docker Web](https://www.docker.com/products/docker-desktop/)
2. Install an IDE - Example: [VSCode via Homebrew](https://formulae.brew.sh/cask/visual-studio-code) or [VSCode](https://code.visualstudio.com/)
3. Make sure you can access OpenAI-platform - [OpenAI Platform](https://platform.openai.com/)
4. Access your Datadog Sandbox Environment

***Doghouse Tree***
```
.
├── Dockerfile
├── app.py
├── docker-compose.yaml
├── doghouse
│   ├── chatbot.py
│   ├── designer.py
│   ├── models.py
│   └── routes.py
├── favicon.ico
├── requirements.txt
├── static
│   ├── css
│   │   └── styles.css
│   └── img
│       ├── classic_doghouse.png
│       ├── deluxe_doghouse.png
│       ├── doghouse_logo.png
│       ├── favicon.png
│       └── portable_doghouse.png
└── templates
    ├── about.html
    ├── base.html
    ├── chatbot.html
    ├── checkout.html
    ├── confirm.html
    ├── designer.html
    ├── home.html
    ├── product.html
    ├── products.html
    └── result.html

```

### Instructions

1. Clone/Download the doghouse-store repository.
2. Get your Datadog Sandbox environment ready. (If you are using .EU, you will have to specify this through out the exercise.)
   - Generate/Copy and save an API Key to use during the exercise
3. Move on to Section 1.
