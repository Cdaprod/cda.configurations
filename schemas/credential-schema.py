from pydantic import BaseModel, SecretStr
from typing import Optional, Dict
from models import CredentialType

class CredentialBase(BaseModel):
    name: str
    type: CredentialType
    details: Optional[Dict[str, str]] = None

class CredentialCreate(CredentialBase):
    value: SecretStr

class Credential(CredentialBase):
    value: str

    class Config:
        orm_mode = True
        
