# config/credentials.py
from cryptography.fernet import Fernet

class CredentialManager:
    # Your secret encryption key
    _CRYPTO_KEY = b'v4XmUNiydR4qyxe0gRg7EKbd9c0q4neeXnk287hrHfk='
    _FERNET = Fernet(_CRYPTO_KEY)

    # Encrypted credentials
    _ENCRYPTED_EMAIL = b'gAAAAABoVXNqj9wasjTBJa_vEycQged89ZuXROqhD03LYefTu-JuvaNxtlWJpBs9CQRlMeyvG2U3pTAUxAEk5yK7eU4K_BUMAKIE-zv51STC5ASKmJ1XVq0='
    _ENCRYPTED_PASSWORD = b'gAAAAABoVXNq07t_wR4l8xabJGZB3krUj0_IsW5Z7dHrMPH1kThSf1uURqONVZTJHPp8hEGHjzc3OUXWy_HRTvayI8XKGmlawg=='

    @classmethod
    def get_credentials(cls):
        return {
            "username": cls._FERNET.decrypt(cls._ENCRYPTED_EMAIL).decode(),
            "password": cls._FERNET.decrypt(cls._ENCRYPTED_PASSWORD).decode()
        }
