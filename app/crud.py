from sqlalchemy.orm import Session
from . import models, schemas

def create_borrower(db: Session, borrower: schemas.BorrowerCreate):
    new_borrower = models.Borrower(name=borrower.name, email=borrower.email)
    db.add(new_borrower)
    db.commit()
    db.refresh(new_borrower)
    return new_borrower

def create_loan(db: Session, loan: schemas.LoanCreate):
    new_loan = models.Loan(**loan.dict())
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan

def get_loans(db: Session, borrower_id: int):
    return db.query(models.Loan).filter(models.Loan.borrower_id == borrower_id).all()
