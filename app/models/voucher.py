from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database.db import Base


class Voucher(Base):
    __tablename__ = "vouchers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    brand = Column(String)
    category = Column(String)
    original_price = Column(Float)
    selling_price = Column(Float)
    description = Column(String)
    code = Column(String, unique=True)
    is_available = Column(Boolean, default=True)
