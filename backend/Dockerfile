FROM python:3

RUN mkdir -p /app
WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn -k uvicorn.workers.UvicornWorker \
 --bind "0.0.0.0:5000" --log-level debug main:app

