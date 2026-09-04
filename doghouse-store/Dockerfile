FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["ddtrace-run", "python", "-m", "app"]
