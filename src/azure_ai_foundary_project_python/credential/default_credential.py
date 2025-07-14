from .base_credential import BaseCredential
from azure.identity import DefaultAzureCredential
from dataclasses import dataclass, field

@dataclass
class DefaultCredential(BaseCredential):
    """Default implementation of the credential using DefaultAzureCredential."""
    credential: DefaultAzureCredential = field(default_factory=DefaultAzureCredential)

    def get_credential(self):
        """Returns the Azure credential instance."""
        return self.credential