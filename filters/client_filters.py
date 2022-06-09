from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import BoundFilter


# privte chat filter
class IsPrivate(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.chat.ChatType.PRIVATE


def register_client_filters(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
