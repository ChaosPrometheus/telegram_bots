import logging
logging.basicConfig(level=logging.INFO)
from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
    await message.delete()

@dp.message_handler(content_types=["left_chat_member"])
async def wtulo(message: types.Message):
    await message.delete()

@dp.message_handler(content_types=["new_chat_title"])
async def nct(message: types.Message):
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)