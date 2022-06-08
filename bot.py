from aiogram import Bot, Dispatcher
from aiogram import types, executor
import gspread

room_id = -736029059




@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = hello
    await bot.send_message(message.from_user.id, text)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, content_types=['text', 'photo', 'file', 'voice', 'video'])
async def forward_all(message: types.Message):
    await bot.forward_message(room_id, message.chat.id, message.message_id)


executor.start_polling(dp, skip_updates=False)
