FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
# PARA QUE MUESTRE EN CONSOLA

ENV WEBAPP_DIR=/webapp

RUN mkdir $WEBAPP_DIR

WORKDIR $WEBAPP_DIR

ADD ./requirements.txt $WEBAPP_DIR/

RUN pip install -r ./requirements.txt

ADD . $WEBAPP_DIR/