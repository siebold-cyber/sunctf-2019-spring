FROM python:3

COPY . /app
WORKDIR /app

RUN apt update
RUN apt install -y python3 python3-pip
RUN pip3 install pipenv

RUN pipenv install --system --deploy

CMD ["python3", "src/app.py"]
