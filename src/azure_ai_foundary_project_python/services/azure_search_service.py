from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv
import os
from azure.search.documents import SearchClient
from ..credential import ProjectCredential

load_dotenv(find_dotenv())

NAME = os.getenv("AZURE_SEARCH_SERVICE_NAME", "azure-search-service")
RG = os.getenv("PROJECT_RESOURCE_GROUP", "cfxmlid-fine-tuning-rg")
SKU = os.getenv("AZURE_SEARCH_SERVICE_SKU", "free")
LOC = os.getenv("PROJECT_LOCATION", "eastus-2")
ENDPOINT = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
API_VERSION = os.getenv("AZURE_SEARCH_SERVICE_API_VERSION")
INDEX_NAME = os.getenv("AZURE_SEARCH_SERVICE_INDEX_NAME")
CRED = ProjectCredential()


@dataclass
class AzureSearchService:
    """Azure Search Service configuration."""

    name: str = NAME
    resource_group: str = RG
    endpoint: str = ENDPOINT
    api_version: str = API_VERSION
    index_name: str = INDEX_NAME

    def __post_init__(self):
        if not self.endpoint or not self.index_name:
            raise ValueError("Endpoint and index name must be provided.")

    @property
    def client(self):
        """Returns the Azure Search client."""
        return SearchClient(
            endpoint=self.endpoint,
            index_name=self.index_name,
            credential=CRED(),
            api_version=self.api_version,
        )

    def validate(self):
        """Validates that the service is configured correctly."""
        if not self.name:
            raise ValueError("Service name must be provided.")
        if not self.resource_group:
            raise ValueError("Resource group must be provided.")
        if not self.endpoint:
            raise ValueError("Endpoint must be provided.")
        if not self.api_version:
            raise ValueError("API version must be provided.")
        if not self.index_name:
            raise ValueError("Index name must be provided.")
        

        
