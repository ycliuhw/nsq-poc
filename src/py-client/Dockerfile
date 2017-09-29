FROM python:2.7-alpine

MAINTAINER ycliuhw@gmail.com

ADD requirements.txt /opt/app/requirements.txt
ADD main.py /opt/app/main.py
WORKDIR /opt/app
RUN pip install -r requirements.txt

CMD ["python", "-u", "/opt/app/main.py"]
