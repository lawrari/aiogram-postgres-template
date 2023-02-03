from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime

from bot.db.base import Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String(255), unique=True, nullable=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    role = Column(String(255), nullable=False)
    balance = Column(Integer, nullable=False)
    is_blocked = Column(Boolean, nullable=False)
    invited_by = Column(BigInteger, nullable=True)


    def __repr__(self):
        return f'<User {self.username}>'
