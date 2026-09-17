FROM python:3.11-slim
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY app /usr/src/app/app

EXPOSE 5000
CMD ["python", "-m", "app.app"]
