from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.database.db import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    voucher_id = Column(Integer, ForeignKey("vouchers.id"))

    amount = Column(Float, nullable=False)
    status = Column(String, default="success")  # success / failed