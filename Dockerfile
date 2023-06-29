FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./model /app/model
COPY ./main.py /app/main.py
COPY ./logs /app/logs
COPY ./config.py /app/config.py
COPY ./worker.py /app/worker.py

CMD ["uvicorn", "main:app", \
     "--host", "0.0.0.0", \
     "--port", "80"]