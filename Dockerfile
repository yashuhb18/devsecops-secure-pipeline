FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN useradd -m appuser

USER appuser

CMD ["python","app/app.py"]