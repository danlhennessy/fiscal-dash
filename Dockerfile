FROM python:3.10
COPY src /app/src
COPY run.py /app
COPY requirements /app/requirements
COPY tests /app/tests
WORKDIR /app

ENV DOCKER_ENV true

RUN pip install -r requirements/base.txt
RUN mkdir -p /logs

EXPOSE 5000

CMD ["python", "run.py"]
