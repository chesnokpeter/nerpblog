FROM python:3.11.8-bookworm

COPY . .

RUN apt-get update && \
    apt-get install nodejs -y --no-install-recommends && \
    apt-get install npm -y --no-install-recommends --fix-missing

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN npm install && \
    npm run build

ENV DB_URL="none"
ENV ADMIN_USER="nerpadmin" 
ENV ADMIN_PASS="nerp"

EXPOSE 9100

CMD ["uvicorn", "nerpblog:app", "--port", "9100", "--host", "0.0.0.0"]
