import models
from utils import setup_logger
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

logger = setup_logger("CredKeeperEngine")

# Add a new credential
def create_credential(db: Session, credential: models.Credential):
    try:
        db_credential = models.CredentialDB(
            # Your existing logic
        )
        db.add(db_credential)
        db.commit()
        db.refresh(db_credential)
        return db_credential
    except SQLAlchemyError as e:
        logger.error(f"Error creating credential: {e}")
        db.rollback()
        raise

# Retrieve a credential by name
def get_credential(db: Session, name: str):
    return db.query(models.CredentialDB).filter(models.CredentialDB.name == name).first()

# Retrieve all credentials
def get_credentials(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CredentialDB).offset(skip).limit(limit).all()

# Update a credential
def update_credential(db: Session, name: str, credential: models.Credential):
    db_credential = get_credential(db, name)
    if db_credential:
        db_credential.type = credential.type
        db_credential.value = credential.value.get_secret_value()
        db_credential.details = credential.details
        db.commit()
        db.refresh(db_credential)
    return db_credential

# Delete a credential
def delete_credential(db: Session, name: str):
    db_credential = get_credential(db, name)
    if db_credential:
        db.delete(db_credential)
        db.commit()
        return db_credential