import os

db_connect = os.environ.get('DB_URL') 
bot_token = os.environ.get('BOT_TOKEN') 

flask_secret_key = 'flasksecret'

admin_username = os.environ.get('ADMIN_USER') 
admin_password = os.environ.get('ADMIN_PASS')

if not admin_username and not admin_password:
    admin_username = 'nerpadmin'
    admin_password = 'nerp'