from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, engine
from database import SessionLocal, db_engine, Base
from utils import setup_logger

# Setting up Logger
logger = setup_logger("CredKeeper")

Base.metadata.create_all(bind=db_engine)

app = FastAPI(title="CredKeeper", description="Manage your credentials securely", version="1.0.0")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/credentials/", response_model=schemas.Credential)
def create_credential(credential: schemas.CredentialCreate, db: Session = Depends(get_db)):
    db_credential = engine.get_credential(db, name=credential.name)
    if db_credential:
        raise HTTPException(status_code=400, detail="Credential already registered")
    return engine.create_credential(db=db, credential=credential)

@app.get("/credentials/{name}", response_model=schemas.Credential)
def read_credential(name: str, db: Session = Depends(get_db)):
    db_credential = engine.get_credential(db, name=name)
    if db_credential is None:
        raise HTTPException(status_code=404, detail="Credential not found")
    return db_credential

@app.get("/credentials/", response_model=list[schemas.Credential])
def read_credentials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    credentials = engine.get_credentials(db, skip=skip, limit=limit)
    return credentials

@app.put("/credentials/{name}", response_model=schemas.Credential)
def update_credential(name: str, credential: schemas.CredentialCreate, db: Session = Depends(get_db)):
    db_credential = engine.get_credential(db, name=name)
    if db_credential is None:
        raise HTTPException(status_code=404, detail="Credential not found")
    return engine.update_credential(db, name, credential)

@app.delete("/credentials/{name}", response_model=schemas.Credential)
def delete_credential(name: str, db: Session = Depends(get_db)):
    db_credential = engine.get_credential(db, name=name)
    if db_credential is None:
        raise HTTPException(status_code=404, detail="Credential not found")
    return engine.delete_credential(db, name)

@app.get("/healthcheck")
def health_check():
    logger.info("Health check request received")
    return {"status": "healthy"}