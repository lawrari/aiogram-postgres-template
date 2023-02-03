from aiogram.filters import BaseFilter
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.requests import get_user


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message, session: AsyncSession):
        return (await get_user(session, message.from_user.id)).role == "admin"
