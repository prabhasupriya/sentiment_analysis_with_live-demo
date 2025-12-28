FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=300 -r requirements.txt

COPY . .

CMD ["python", "ingester.py"]
