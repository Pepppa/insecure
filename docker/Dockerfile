FROM python:3.5
COPY docker/requirements.txt /
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
COPY src/*  /
COPY docker/entry_point.sh  /
CMD [ "/entry_point.sh" ]
