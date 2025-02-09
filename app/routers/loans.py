from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.LoanResponse)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(database.get_db)):
    return crud.create_loan(db, loan)

@router.get("/{borrower_id}", response_model=list[schemas.LoanResponse])
def get_loans(borrower_id: int, db: Session = Depends(database.get_db)):
    loans = crud.get_loans(db, borrower_id)
    if not loans:
        raise HTTPException(status_code=404, detail="No loans found")
    return loans
