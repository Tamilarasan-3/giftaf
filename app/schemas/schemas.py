from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str

from pydantic import BaseModel

class VoucherCreate(BaseModel):
    title: str
    brand: str
    category: str
    original_price: float
    selling_price: float
    description: str
    code: str  

