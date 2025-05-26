FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY bank_expense_etl_pipeline.py ./
COPY data/ ./data/
RUN mkdir -p /output

CMD ["python", "bank_expense_etl_pipeline.py"]
