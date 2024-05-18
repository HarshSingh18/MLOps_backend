FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY flask_app.py .
COPY House_Rent_Dataset.csv .
EXPOSE 5000

CMD ["python", "flask_app.py"]
