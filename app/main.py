from fastapi import FastAPI
from app.routers import borrowers, loans
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(borrowers.router, prefix="/borrowers", tags=["Borrowers"])
app.include_router(loans.router, prefix="/loans", tags=["Loans"])
