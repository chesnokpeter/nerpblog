import os

db_connect = os.environ.get('DB_URL') 
bot_token = os.environ.get('BOT_TOKEN') 

flask_secret_key = 'flasksecret'