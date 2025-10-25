FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    mkdir -p app

WORKDIR app

COPY . .

RUN python3 -m pip install --break-system-packages -r ./requirements.txt


ENTRYPOINT python3 src/app/main.py