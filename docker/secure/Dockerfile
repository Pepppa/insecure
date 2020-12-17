FROM python:3.5
COPY docker/site/requirements.txt /
RUN pip install -r requirements.txt
EXPOSE 5001/tcp
COPY src/py/*  /
CMD [ "python", "-u", "server_secure.py" ]
