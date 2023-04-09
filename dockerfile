FROM python:latest

#create non root user to own files
RUN useradd -m -u 1000 watchcat
WORKDIR /home/watchcat

#copy data
COPY src/ ./

#install dependecies
RUN python3 -m pip install -r requirements.txt

#start
CMD [ "python3", "main.py" ]