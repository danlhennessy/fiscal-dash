FROM python:3.10
COPY src /app/src
COPY run.py /app
COPY requirements /app/requirements
COPY tests /app/tests
COPY logs /app/logs
WORKDIR /app

ENV DOCKER_ENV true

RUN pip install -r requirements/base.txt

EXPOSE 5000

CMD ["python", "run.py"]
