import multiprocessing
import asyncio
import logging
import uvicorn
import sys
from nerpblog.bot.bot import main as bot_run

def server() -> None:
    uvicorn.run('nerpblog:app', port=9100, host='0.0.0.0')

def bot() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.create_task(bot_run())
    loop.run_forever()

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=server)
    process2 = multiprocessing.Process(target=bot)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
