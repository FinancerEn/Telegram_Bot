from sqlalchemy import Column, String, Text, Float, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    # Время создания записи, при изменениях фиксируем дату
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    image = Column(String(150), nullable=True)


# модель для файла inlaine_logice.py
class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(nullable=False)  # ID пользователя Telegram
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    platform: Mapped[str] = mapped_column(String(50), nullable=False)  # Выбранная платформ
    bot_type: Mapped[str] = mapped_column(String(100), nullable=False)  # Тип бота
    wishes: Mapped[Text] = mapped_column(Text, nullable=True)  # Пожелания
    functional: Mapped[Text] = mapped_column(Text, nullable=True)
    contacts: Mapped[str] = mapped_column(String(255), nullable=False)
