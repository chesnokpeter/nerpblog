# FROM python:3.11.4-alpine
# FROM node:20.11.0
# # FROM npm:10.2.4 

# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# COPY . .

# RUN apk add --no-cache py-pip

# RUN pip3 install -r drequirements.txt
# RUN npm install
# RUN npm run build

# ENV BOT_TOKEN "none"
# ENV DB_URL "none"

# EXPOSE 9001

# CMD [ "/usr/bin/supervisord" ]


FROM python:3.11.4-alpine

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY . .

RUN apk add --no-cache nodejs npm py-pip

RUN ls
RUN pip install -r drequirements.txt
RUN npm install
RUN npm run build

ENV BOT_TOKEN="none"
ENV DB_URL="none"

EXPOSE 9001

CMD [ "/usr/bin/supervisord" ]
