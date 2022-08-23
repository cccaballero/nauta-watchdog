FROM python:3.9-alpine
RUN apk update \
  && apk add \
    git
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY . .
RUN addgroup -g 1000 -S nconnect && \
    adduser -u 1000 -S nconnect -G nconnect
USER nconnect
CMD ["python", "main.py"]
