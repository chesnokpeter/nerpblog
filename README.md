![nerpblog](nerpblog/public/cover.png)
## nerpblog is a open-source proj post publishing
### with deep integration via Telegram
#### Open&Free&NoAds
on the nerpblog you can see the posts, put a like, there is also a page of a particular post\
**you can write a post using a telegram bot, and the markup inside the post message is saved**
- vue js
- vite
- PWA
- fastapi
- flask admin
- aiogram
- sqlalchemy
- postgresql
### future features
- [x] ~~photo in post~~
- [x] ~~comments via tg bot~~
- [x] ~~complete function tg bot~~
- [x] ~~admin panel~~
- [ ] tg instants view
- [x] ~~complete PWA~~
- [ ] docker container
- [ ] ***deploy!***
---
### install 
#### docker:
coming soon `¯\_(ツ)_/¯`
#### linux: 
1. `git clone https://github.com/chesnokpeter/nerpblog.git`
2. `cd nerpblog`
3. `python3 venv venv`
4. `source venv/bin/activate`
5. `pip3 install -r requirements.txt`
6. `npm install`
#### windows
1. `git clone https://github.com/chesnokpeter/nerpblog.git`
2. `cd nerpblog`
3. `python -m venv venv`
4. `venv/Scripts/activate`
5. `pip install -r requirements.txt`
6. `pip install psycopg2`
7. `npm install`
### develop
`source venv/bin/activate` or `venv/Scripts/activate` on windows\
#### set environ variables BOT_TOKEN, DB_URL, ADMIN_USER, ADMIN_PASS
    $env:BOT_TOKEN=[ TOKEN ]"" (PS windows )
    export DB_URL=[ URL ] (linux)
backend: `uvicorn nerpblog:app --port 9001 --reload --host 0.0.0.0`\
frontend: `npm run dev`\
bot: `python nerpblog/bot`
### production
coming soon `¯\_(ツ)_/¯`
### config:
`production port: 9100`\
`backend port: 9001`\
`frontend port: 9002`\
`python 3.11.4` \
`npm 10.2.4` \
`node 20.11.0`\
**environ variables:**\
***DB_URL*** url to the database\
***BOT_TOKEN*** telegram bot token\
***ADMIN_USER*** *default:* `nerpadmin` | flask admin interface panel user\
***ADMIN_PASS*** *default:* `nerp` | flask admin interface panel password



