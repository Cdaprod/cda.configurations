import os
import logging
from cryptography.fernet import Fernet

# Environment Variable Management
def get_environment_variable(key: str, default=None):
    return os.environ.get(key, default)

# Logging Utility
def setup_logger(name: str, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    stream_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(stream_handler)
    
    return logger

# Encryption Utilities
class EncryptionUtility:
    @staticmethod
    def generate_key() -> str:
        return Fernet.generate_key().decode()

    @staticmethod
    def encrypt_message(message: str, key: str) -> str:
        f = Fernet(key.encode())
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message.decode()

    @staticmethod
    def decrypt_message(encrypted_message: str, key: str) -> str:
        f = Fernet(key.encode())
        decrypted_message = f.decrypt(encrypted_message.encode())
        return decrypted_message.decode()

# Additional utilities can be added here based on your application's requirements