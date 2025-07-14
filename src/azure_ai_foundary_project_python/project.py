import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass, field
from .credential import BaseCredential, DefaultCredential

load_dotenv(find_dotenv())

PROJECT_NAME = os.getenv("PROJECT_NAME", "azure-ai-foundary-project-python")
PROJECT_ENDPOINT = os.getenv("AZURE_AI_PROJECT_ENDPOINT")

@dataclass
class Project:
    name: str = PROJECT_NAME
    endpoint: str = PROJECT_ENDPOINT
    cred: BaseCredential = field(default_factory=DefaultCredential)
