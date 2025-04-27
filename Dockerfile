FROM python:3.10-slim

LABEL authors="Arslon"

WORKDIR /app

COPY app/ /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
