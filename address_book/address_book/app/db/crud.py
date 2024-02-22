from sqlalchemy.orm import Session
from . import models, schemas


def create_address(db: Session, address: schemas.AddressCreate):
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def get_address(db: Session, address_id: int):
    return db.query(models.Address).filter(models.Address.id == address_id).first()


def update_address(db: Session, db_address: models.Address, address: schemas.AddressUpdate):
    for attr, value in address.dict(exclude_unset=True).items():
        setattr(db_address, attr, value)
    db.commit()
    db.refresh(db_address)
    return db_address


def delete_address(db: Session, db_address: models.Address):
    db.delete(db_address)
    db.commit()
