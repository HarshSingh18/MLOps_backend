FROM python:3.11-slim

WORKDIR /app

COPY House_Rent_Dataset.csv .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY flask_app.py .

EXPOSE 5000

CMD ["python", "flask_app.py"]
