# Use an official Python runtime based on Alpine as a parent image
FROM python:3.12.1-alpine
WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
