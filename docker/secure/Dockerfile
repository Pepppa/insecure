FROM python:3.5
COPY docker/secure/requirements.txt /
RUN pip install -r requirements.txt
EXPOSE 5001/tcp

RUN apt-get -y update && \
    apt-get -y --no-install-recommends install --fix-missing openssh-server && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /src
COPY src/py/server_secure.py  /src/.
COPY src/py/passwd.py  /src/.
COPY src/py/db.py  /src/.

COPY docker/secure/data_entry_point.sh  /src/

CMD [ "/src/data_entry_point.sh" ]
