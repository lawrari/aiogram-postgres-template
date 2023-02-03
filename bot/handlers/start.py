from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.requests import create_user, get_user
from bot.filters.admin import AdminFilter

router = Router()
router.message.filter(Command(commands=["start"]))

@router.message(AdminFilter())
async def admin_start(message: Message):
    kb = [
        [types.KeyboardButton(text="🛒 Каталог")],
        [types.KeyboardButton(text="👤 Профиль")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Hello, admin!", reply_markup=keyboard)


@router.message()
async def start(message: Message, session: AsyncSession):
    user = await get_user(session, message.from_user.id)
    if not user:
        user = await create_user(
            session,
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
            None
        )
    kb = [
        [types.KeyboardButton(text="🛒 Каталог")],
        [types.KeyboardButton(text="👤 Профиль")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=keyboard)
