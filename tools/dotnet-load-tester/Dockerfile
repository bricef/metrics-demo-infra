FROM python:3.6-jessie

RUN pip install locustio

ADD locustfile.py .

ENTRYPOINT ["locust", "-H", "dotnet-prometheus-example.default", "--no-web", "-c", "1000", "-r", "1"]




