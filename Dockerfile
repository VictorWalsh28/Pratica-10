FROM python:3.11-slim
WORKDIR /usr/src/app

COPY requirements-dev.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY app /usr/src/app/app

EXPOSE 5000
CMD ["python", "-m", "app.app"]
