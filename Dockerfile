FROM python:3.10

WORKDIR /app

COPY requirements.txt app.py ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]