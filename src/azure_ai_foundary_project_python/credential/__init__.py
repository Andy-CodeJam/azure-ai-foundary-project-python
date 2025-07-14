from .base_credential import BaseCredential
from .default_credential import DefaultCredential
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
PROJECT_CREDENTIAL_TYPE = os.getenv("PROJECT_CREDENTIAL_TYPE", "default")


__all__ = [
    "BaseCredential",
    "DefaultCredential",
]
