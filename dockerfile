FROM python:latest

RUN mkdir -p /usr/
WORKDIR /usr/src/
COPY src/ ./

RUN python3 -m pip install -r requirements.txt


CMD [ "python3", "main.py" ]