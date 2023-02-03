from contextlib import suppress
from datetime import datetime
from typing import List

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.models import User


async def create_user(session: AsyncSession, user_id: int, username: str, first_name: str, last_name: str, invited_by: int) -> User:
    user = User(
        user_id=user_id,
        username=username,
        first_name=first_name,
        last_name=last_name,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        role="user",
        balance=0,
        is_blocked=False,
        invited_by=None,
    )
    session.add(user)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
    return user


async def get_user(session: AsyncSession, user_id: int) -> User:
    user = await session.execute(select(User).filter_by(user_id=user_id))
    return user.scalar()


async def get_users(session: AsyncSession, user_ids: List[int]) -> List[User]:
    users = await session.execute(select(User).filter(User.user_id.in_(user_ids)))
    return users.scalars().all()


async def edit_user(session: AsyncSession, user_id: int, **kwargs) -> User:
    user = await get_user(session, user_id)
    for key, value in kwargs.items():
        setattr(user, key, value)
    await session.commit()
    return user
