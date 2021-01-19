FROM python:3.5
COPY docker/site/requirements.txt /
RUN pip install -r /requirements.txt
EXPOSE 5000/tcp

RUN apt-get -y update && \
    apt-get -y --no-install-recommends install --fix-missing openssh-server && \
    rm -rf /var/lib/apt/lists/*

RUN touch /var/log/security_events.log && \
    chmod 666 /var/log/security_events.log

RUN mkdir /src && \
    chmod 700 /src
COPY src/py/*  /src/

RUN mkdir -p /src/static/
COPY src/js/*  /src/static/
COPY src/css/*  /src/static/
COPY favicon.ico /src/static/
COPY docker/site/entry_point.sh  /src/

CMD [ "/src/entry_point.sh" ]
