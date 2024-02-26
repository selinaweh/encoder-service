FROM python:3.12-slim-bookworm

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8002
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8002"]
