from pydantic import BaseModel, EmailStr, Field, validator
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
    amount: float = Field(gt=0, description="Сумма займа должна быть больше 0")
    interest_rate: float = Field(ge=0, description="Процентная ставка не может быть отрицательной")
    start_date: date
    end_date: date

    @validator("start_date")
    def validate_start_date(cls, v):
        today = date.today()
        if v < today:
            raise ValueError("Дата начала займа не может быть раньше сегодняшней")
        return v

    @validator("end_date")
    def validate_end_date(cls, v, values):
        if "start_date" in values and v < values["start_date"]:
            raise ValueError("Дата окончания займа не может быть раньше даты начала")
        return v


class LoanResponse(LoanCreate):
    id: int

    class Config:
        from_attributes = True
