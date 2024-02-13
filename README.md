![nerpblog](nerpblog/public/cover.png)
## nerpblog is a open-source proj post publishing
### with deep integration via Telegram
on the nerpblog you can see the posts, put a like, there is also a page of a particular post\
**you can write a post using a telegram bot, and the markup inside the post message is saved**
- vue js
- vite
- fastapi
- aiogram
- sqlalchemy
- postgresql
### future features
- [ x ] complete /prog, /about
- [ ] photo in post
- [ ] docker container
- [ ] comments via tg bot
- [ ] tg instants view
- [ ] complete function tg bot
- [ ] complete PWA
- [ ] admin panel
- [ ] ***deploy!***
---
### install 
1. `git clone https://github.com/chesnokpeter/nerpblog.git`
2. `cd nerpblog`
3. `py -3.11 -m venv venv`
4. `source venv/bin/activate` or `venv/Scripts/activate`(windows)
5. `pip install -r requirements.txt`
6. set environ variables BOT_TOKEN, DB_URL\
`$env:BOT_TOKEN=""` (PS windows )\
`export DB_URL=` (linux)
7. `npm install`
### develop
`source venv/bin/activate (venv/Scripts/activate on windows)`\
backend: `py -m uvicorn nerpblog:app --port 9001 --reload --host 0.0.0.0`\
frontend: `npm run dev`\
bot: `py nerpblog/bot.py`
### production
coming soon `¯\_(ツ)_/¯`
### config:
    backend port: 9001
    frontend port: 9002
    python 3.11.4 
    npm 10.2.4 




