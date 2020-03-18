FROM python:3

RUN apt-get -yqq update
RUN apt-get -yqq install python-pip python-dev curl

COPY requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR /src
COPY ./app .

CMD python3 main.py --host 0.0.0.0
