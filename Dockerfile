FROM python:3.11.8-bookworm

COPY . .

RUN apt-get update 
RUN apt-get install -y supervisor
RUN apt-get install nodejs -y --no-install-recommends
RUN apt-get install npm -y --no-install-recommends --fix-missing
RUN mkdir -p /var/log/supervisor
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt 
RUN npm install 
RUN npm run build

ENV BOT_TOKEN="none"
ENV DB_URL="none"

EXPOSE 9001

CMD ["python", "main.py"]
