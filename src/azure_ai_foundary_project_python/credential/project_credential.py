from .base_credential import BaseCredential
from .default_credential import DefaultCredential
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
PROJECT_CREDENTIAL_TYPE = os.getenv("PROJECT_CREDENTIAL_TYPE", "default")

class ProjectCredential(BaseCredential):
    """Project-specific credential class that selects the appropriate credential type."""

    def __init__(self):
        if PROJECT_CREDENTIAL_TYPE == "default":
            self.credential = DefaultCredential()
        else:
            self.credential = BaseCredential()

    def get_credential(self):
        """Returns the selected credential instance."""
        return self.credential.get_credential()