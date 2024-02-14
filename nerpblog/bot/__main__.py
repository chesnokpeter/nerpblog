import sys
sys.path[0] = sys.path[0].split('nerpblog')[0]+'nerpblog'+sys.path[0].split('nerpblog')[1]
print(sys.path)
import asyncio
import logging
from nerpblog.bot.bot import main
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
