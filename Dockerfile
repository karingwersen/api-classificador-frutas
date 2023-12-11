FROM python:3.11

COPY requirements.txt ./requirements.txt

RUN mkdir /app

COPY ./api /app/

COPY ./container_startup_script.sh /tmp/container_startup_script.sh

RUN chmod +x /tmp/container_startup_script.sh

RUN python3 -m pip install -r requirements.txt

WORKDIR /app

ENTRYPOINT [ "/tmp/container_startup_script.sh" ]