from fastapi import FastAPI, Depends
from fastapi import FastAPI
from app.api.routes import router
from app.database.db import engine, Base
from app.models.voucher import Voucher
from app.models.transaction import Transaction

app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(router)

