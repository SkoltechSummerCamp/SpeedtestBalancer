FROM python:3.6-alpine

EXPOSE 8080

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY server/ /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

CMD python3 setup.py install --user

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]