FROM python:3.9-slim
WORKDIR /code
COPY app.py preStop.sh ./
CMD [ "python", "./app.py"]
