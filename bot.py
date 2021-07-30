import config
import logging
import functions
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("I'm url shortener bot\nhttps://www.flipkart.com/search?q=dress&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off = https://cutt.ly/HQdvIdS\nSend me Link👇")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(functions.get_url(message.text))
if __name__ == '__main__':
    print("Ok...")
    executor.start_polling(dp, skip_updates=True)
