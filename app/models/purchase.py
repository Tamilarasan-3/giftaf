from sqlalchemy import Column, Integer, ForeignKey
from app.database.db import Base


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    voucher_id = Column(Integer, ForeignKey("vouchers.id"))