from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.database.db import get_db
from app.models.user import User
from app.models.voucher import Voucher
from app.schemas.schemas import LoginRequest
from app.models.transaction import Transaction
from app.schemas.schemas import VoucherCreate

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

router = APIRouter()


# ---------------- AUTH ---------------- #

@router.post("/signup")
def signup(user: LoginRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    new_user = User(
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}


@router.post("/login")
def login(user: LoginRequest, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user or not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token({
        "sub": user.email
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/profile")
def profile(current_user: str = Depends(get_current_user)):
    return {
        "message": "You are logged in",
        "user": current_user
    }


# ---------------- VOUCHERS ---------------- #

@router.post("/vouchers")
def create_voucher(
    title: str,
    brand: str,
    category: str,
    original_price: float,
    selling_price: float,
    description: str,
    code: str,
    db: Session = Depends(get_db)
):
    existing_voucher = db.query(Voucher).filter(
        Voucher.code == code
    ).first()

    if existing_voucher:
        raise HTTPException(
            status_code=400,
            detail="Voucher code already exists"
        )

    voucher = Voucher(
        title=title,
        brand=brand,
        category=category,
        original_price=original_price,
        selling_price=selling_price,
        description=description,
        code=code
    )

    db.add(voucher)
    db.commit()
    db.refresh(voucher)

    return {
        "message": "Voucher created successfully",
        "voucher_id": voucher.id
    }


@router.get("/vouchers")
def get_vouchers(db: Session = Depends(get_db)):
    vouchers = db.query(Voucher).filter(
        Voucher.is_available == True
    ).all()

    return vouchers

@router.get("/my-vouchers")
def my_vouchers(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # get logged-in user
    user = db.query(User).filter(
        User.email == current_user
    ).first()

    # fetch vouchers purchased by this user
    vouchers = db.query(Voucher).filter(
        Voucher.user_id == user.id
    ).all()

    return vouchers

@router.post("/vouchers")
def create_voucher(
    voucher: VoucherCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(Voucher).filter(
        Voucher.code == voucher.code
    ).first()

    if existing:
        raise HTTPException(400, "Code exists")

    new_voucher = Voucher(**voucher.dict())

    db.add(new_voucher)
    db.commit()
    db.refresh(new_voucher)

    return new_voucher

@router.post("/buy/{voucher_id}")
def buy_voucher(
    voucher_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # get logged-in user
    user = db.query(User).filter(
        User.email == current_user
    ).first()

    # get voucher
    voucher = db.query(Voucher).filter(
        Voucher.id == voucher_id,
        Voucher.is_available == True
    ).first()

    # check if exists
    if not voucher:
        raise HTTPException(404, "Voucher not available")

    # assign voucher to user
    voucher.user_id = user.id
    voucher.is_available = False

    # create transaction
    transaction = Transaction(
        user_id=user.id,
        voucher_id=voucher.id,
        amount=voucher.selling_price
    )

    db.add(transaction)
    db.commit()

    return {"message": "Voucher purchased successfully"}