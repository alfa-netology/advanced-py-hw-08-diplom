from application.settings import api_token
from application.classes.bot import Bot

bot = Bot(api_token)
bot.start()

