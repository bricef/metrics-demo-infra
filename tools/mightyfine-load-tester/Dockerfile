FROM python:3.6-jessie

RUN pip install locustio

ADD locustfile.py .

ENTRYPOINT ["locust", "-H", "mighty-fine-fe.default:3000", "--no-web", "-c", "1000", "-r", "1"]




