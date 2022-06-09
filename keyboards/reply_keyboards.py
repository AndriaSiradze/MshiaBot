from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from tg_bot.sheet import get_offices

no_office = KeyboardButton('Нету офиса')
offices_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
offices_kb.add(no_office)
for topic in get_offices():
    topic_button = KeyboardButton(topic)
    offices_kb.insert(topic_button)