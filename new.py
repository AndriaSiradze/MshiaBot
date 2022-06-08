from aiogram import Bot, Dispatcher
from aiogram import types, executor
import gspread
import datetime

room_id = -736029059
bot = Bot(token="5394433986:AAEgMZgnaEkE9wET6vgsvCBDpn-sjWcohZs")
dp = Dispatcher(bot)

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
s_a = gspread.service_account('creds.json', scopes=scopes)

sheet = s_a.open("mshiabot").sheet1
hello = sheet.col_values(1)[-1]


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = hello
    await bot.send_message(message.from_user.id, text)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, content_types=['text', 'photo', 'file', 'voice', 'video'])
async def forward_all(message: types.Message):
    await bot.forward_message(room_id, message.chat.id, message.message_id)


executor.start_polling(dp, skip_updates=False)
