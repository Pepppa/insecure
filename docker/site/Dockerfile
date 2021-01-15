FROM eugenes1/python-sshd
COPY docker/site/requirements.txt /
RUN pip install -r /requirements.txt
EXPOSE 5000/tcp
COPY src/py/*  /
RUN mkdir -p /static
COPY src/js/*  /static/
COPY src/css/*  /static/
COPY favicon.ico /static/
COPY docker/site/entry_point.sh  /
CMD [ "/entry_point.sh" ]
