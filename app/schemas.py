from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List

class BorrowerCreate(BaseModel):
    name: str
    email: EmailStr

class BorrowerResponse(BorrowerCreate):
    id: int

    class Config:
        from_attributes = True

class LoanCreate(BaseModel):
    borrower_id: int
    amount: float
    interest_rate: float
    start_date: date
    end_date: date

class LoanResponse(LoanCreate):
    id: int

    class Config:
        from_attributes = True
