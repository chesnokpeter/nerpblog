import sys
sys.path[0] = sys.path[0]+'/../../'
print(sys.path[0])
import asyncio
import logging
from nerpblog.bot.bot import main
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
