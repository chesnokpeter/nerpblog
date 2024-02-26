FROM node:latest AS node_base

RUN echo "NODE Version:" && node --version
RUN echo "NPM Version:" && npm --version

FROM python:3.11.8-bookworm

COPY --from=node_base . .

COPY . .

RUN apt-get update

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN npm install && \
    npm run build

ENV DB_URL="none"
ENV BOT_TOKEN="none"
ENV ADMIN_USER="nerpadmin" 
ENV ADMIN_PASS="nerp"

EXPOSE 9100

CMD ["uvicorn", "nerpblog:app", "--port", "9100", "--host", "0.0.0.0"]
