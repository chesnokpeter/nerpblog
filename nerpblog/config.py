import os
from nerpblog.app.schemas.exceptions import EnvVariablesExceptions, DbConnectException

db_connect = os.environ.get('DB_URL') 
bot_token = os.environ.get('BOT_TOKEN') 

flask_secret_key = 'flasksecret'

admin_username = os.environ.get('ADMIN_USER') 
admin_password = os.environ.get('ADMIN_PASS')

if not admin_username and not admin_password:
    admin_username = 'nerpadmin'
    admin_password = 'nerp'

bot_username = 'nrpblgbot'
bot_start_deeplink = 'start'

frontend_app = True
admin_app = True

def check_startup():
    if not db_connect or not bot_token:
        raise EnvVariablesExceptions('required variables DB_URL and BOT_TOKEN are not detected')
    if not '+asyncpg' in db_connect:
        raise DbConnectException('connection url db is not asynchronous')

def synchronous_url_db(asyn_url:str) -> str:
    return asyn_url.split('://')[0].replace('+asyncpg', '')+'://'+asyn_url.split('://')[1]