FROM python:3.5
COPY docker/site/requirements.txt /
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
COPY src/py/*  /
COPY src/js/*  /
COPY src/css/*  /
COPY docker/site/entry_point.sh  /
CMD [ "/entry_point.sh" ]
