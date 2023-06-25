FROM python:3.10
COPY src /app/src
COPY run.py /app
COPY requirements /app/requirements
COPY tests /app/tests
WORKDIR /app

ARG VAULT_URL
ARG VAULT_NAMESPACE
ARG VAULT_TOKEN

ENV VAULT_URL=$VAULT_URL
ENV VAULT_NAMESPACE=$VAULT_NAMESPACE
ENV VAULT_TOKEN=$VAULT_TOKEN
ENV DOCKER_ENV true

RUN pip install -r requirements/test.txt

EXPOSE 5000

CMD ["python", "run.py"]
