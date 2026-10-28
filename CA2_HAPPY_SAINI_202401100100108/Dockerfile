FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Dhyan dein: yahan 'main:app' hona chahiye, na ki 'main.py:app'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]