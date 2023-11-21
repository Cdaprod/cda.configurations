from pydantic import BaseModel, Field, SecretStr, validator
from typing import Optional, Dict, Union

class ClientConnection(BaseModel):
    service_name: str = Field(..., description="Name of the service to connect to")
    service_type: str = Field(..., description="Type of service (e.g., 'database', 'api', 'cloud_storage')")
    hostname: Optional[str] = Field(None, description="Hostname of the service")
    port: Optional[int] = Field(None, description="Port to use for the connection")
    username: Optional[str] = Field(None, description="Username for authentication")
    password: Optional[SecretStr] = Field(None, description="Password for authentication")
    api_key: Optional[SecretStr] = Field(None, description="API key for services that require it")
    database_name: Optional[str] = Field(None, description="Name of the database to connect to, if applicable")
    additional_params: Optional[Dict[str, Union[str, int, bool]]] = Field(
        None, description="Additional parameters required for the connection"
    )
    
    @validator('service_type')
    def validate_service_type(cls, v):
        allowed_types = ['database', 'api', 'cloud_storage', 'message_broker', 'custom']
        if v not in allowed_types:
            raise ValueError(f'service_type must be one of {allowed_types}')
        return v
    
    @validator('port')
    def validate_port(cls, v, values, **kwargs):
        if 'hostname' in values and values['hostname'] and (v is None or v <= 0):
            raise ValueError('Port must be a positive integer when hostname is provided')
        return v

    class Config:
        min_anystr_length = 1  # Ensuring that strings are not empty
        anystr_strip_whitespace = True  # Stripping whitespace from strings

# Example usage
connection_details = ClientConnection(
    service_name="My Database Service",
    service_type="database",
    hostname="db.example.com",
    port=5432,
    username="user",
    password=SecretStr("securepassword"),
    database_name="mydatabase"
)

# The logic for actually establishing the connection would be in the respective client modules
