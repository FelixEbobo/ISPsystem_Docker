FROM python:3

EXPOSE 1829

COPY app.py /app.py
COPY index.html /index.html

RUN apt install -y git

CMD [ "/usr/bin/python3",  "app.py", "1829"]