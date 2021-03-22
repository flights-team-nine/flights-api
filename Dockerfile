FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
RUN apk add build-base
RUN apk add libffi-dev
RUN apk add openssl
RUN apk add openssl-dev
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY /requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt