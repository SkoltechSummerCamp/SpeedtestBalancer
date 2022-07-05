FROM ubuntu:20.04

EXPOSE 8080

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN ["apt-get", "update"]
RUN sh -c 'yes | apt-get install gcc python3.8 python3-pip'
RUN ["python3.8", "-m", "pip", "install", "--upgrade", "pip"]
RUN ["pip", "install", "pipenv"]
RUN ["pipenv", "install"]

CMD ["pipenv", "run", "gunicorn", "balancer.wsgi", "-b", ":8080"]
