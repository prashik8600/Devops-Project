FROM python:3.9-slim-buster

WORKDIR /app

COPY requirement.txt .

RUN pip3 install --no-cache-dir -r requirement.txt

COPY . .

ENV FLASK_RUN_HOST=34.230.82.219

EXPOSE 5000

CMD  ["flask", "run"]
