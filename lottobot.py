import logging
logging.basicConfig(level=logging.INFO)
import random
from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher

bot = Bot(token='')
dp = Dispatcher(bot)

@dp.message_handler(commands=['random'])
async def main(message: types.Message):
    number = random.randint(0, 91)
    await bot.send_message(message.chat.id, number)

@dp.message_handler(content_types=["new_chat_members"])
async def send_welcome(message: types.Message):
    await message.reply(
        message.from_user.first_name + "")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)