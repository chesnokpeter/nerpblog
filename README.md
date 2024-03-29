![nerpblog](nerpblog/public/cover.png)
## nerpblog is a open-source proj post publishing
### with deep integration via Telegram
#### Open&Free&NoAds
On **[nerp.blog](https://nerp.blog/)** you can publish posts, give likes, comment, the site is for browsing only.\
Register an account, create posts, write comments, all this available **in telegram bot for protection and usability**.\
Also you can attach **media** in post and use **html markup**.
- vue js
- vite
- PWA
- fastapi
- flask admin
- aiogram
- sqlalchemy
- postgresql
- unit of work
### future features
- [x] **photo in post**
- [x] **comments via tg bot**
- [x] **admin panel**
- [x] **PWA**
- [x] **docker container**
- [x] ***deploy!***
- [ ] tg instants view
- [ ] complete logs and logs webview
- [ ] native mobile client
- [ ] tg custom emoji
- [ ] search indexing
- [ ] tg bot on hooks
- [ ] ssr
---
### install 
#### docker:
run server
```
docker pull chesnokdeep/nerpblog:server
docker run -d -p 9100:9100 -e DB_URL= -e BOT_TOKEN= -e ADMI_USER= -e ADMIN_PASS= chesnokdeep/nerpblog:server
```
run bot
```
docker pull chesnokdeep/nerpblog:bot
docker run -d -e DB_URL= -e BOT_TOKEN= chesnokdeep/nerpblog:bot
```
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
    $env:BOT_TOKEN="[ TOKEN ]" (PS windows )
    export DB_URL=[ URL ] (linux)
backend: `uvicorn nerpblog:app --port 9001 --reload --host 0.0.0.0`\
frontend: `npm run dev`\
bot: `python nerpblog/bot`
### config:
`production port: 9100`\
`backend port: 9001`\
`frontend port: 9002`\
`python 3.11.4` \
`npm 10.2.4` \
`node 20.11.0`\
**environ variables:**\
***`DB_URL`*** - url to the database\
***`BOT_TOKEN`*** - telegram bot token\
***`ADMIN_USER`*** - flask admin interface panel user, *default:* `nerpadmin`\
***`ADMIN_PASS`*** - flask admin interface panel password, *default:* `nerp`



