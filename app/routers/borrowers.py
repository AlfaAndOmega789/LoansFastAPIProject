from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database, models
from typing import List

router = APIRouter()

@router.post("/", response_model=schemas.BorrowerResponse)
def create_borrower(borrower: schemas.BorrowerCreate, db: Session = Depends(database.get_db)):
    return crud.create_borrower(db, borrower)

@router.get("/", response_model=List[schemas.BorrowerResponse])
def get_borrowers(db: Session = Depends(database.get_db)):
    borrowers = db.query(models.Borrower).all()
    return borrowers
