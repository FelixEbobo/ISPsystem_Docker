FROM python:3

EXPOSE 1829

COPY app.py /
COPY cat.gif /
COPY index.html /
COPY entrypoint.sh /
COPY requirenments.txt /

RUN apt update
RUN apt install -y python3-pymysql

ENTRYPOINT [ "/entrypoint.sh" ]