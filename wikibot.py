import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5244411667:AAGJ7SATQM8MmJDXMwCSXtA_c2Cje9bpkfI'
wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
  
    await message.reply("wikipediaga hush kelibsiz")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        respons = wikipedia.summary(message.text)
        await message.answer(respons)
    except:
        await message.answer('bunday maqola yoq')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)