# import logging
# import logging.config

# # Get logging configurations
# logging.config.fileConfig('logging.conf')
# logging.getLogger().setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
# from utils import Media
from dotenv import load_dotenv
import os

load_dotenv()

class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name=os.environ['SESSION'],
            api_id=os.environ['API_ID'],
            api_hash=os.environ['API_HASH'],
            bot_token=os.environ['BOT_TOKEN'],
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        # await Media.ensure_indexes()
        me = await self.get_me()
        self.username = '@' + me.username
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


app = Bot()
app.run()