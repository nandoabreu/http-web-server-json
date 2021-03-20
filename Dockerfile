FROM python:3.6-alpine
COPY server.py /
EXPOSE 5000
CMD python /server.py
