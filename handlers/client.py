from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters.client_filters import IsPrivate
from keyboards.reply_keyboards import offices_kb
from states import StartState
from tg_bot.create_bot import bot
from tg_bot.data import data
from tg_bot.sheet import write_user_info, get_users_list

room_id = -772245161


async def start(message: types.Message):
    user_list = await get_users_list()
    user_id = str(message.from_user.id)
    if user_id in user_list:
        text = data["hello_message"]
        await message.reply(text)
    else:
        text = data["hello_message_newcommers"]
        await message.reply(text, reply_markup=offices_kb)
        await StartState.office.set()


async def set_office(message: types.Message, state: FSMContext):
    text = data["fsm_office_set"]
    await message.reply(text, reply_markup=types.ReplyKeyboardRemove())
    await write_user_info(message)
    await state.finish()


async def forward_all(message: types.Message):
    await bot.forward_message(room_id, message.chat.id, message.message_id)


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start, Command("start"))
    dp.register_message_handler(set_office, state=StartState.office)
    dp.register_message_handler(forward_all, IsPrivate(), content_types=types.ContentTypes.ANY, state=None)
