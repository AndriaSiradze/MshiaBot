from aiogram.dispatcher.filters.state import StatesGroup, State


class StartState(StatesGroup):
    office = State()