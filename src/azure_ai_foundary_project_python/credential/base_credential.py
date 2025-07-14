from abc import ABC, abstractmethod

class BaseCredential(ABC):
    """Abstract base class for credentials."""

    @abstractmethod
    def get_credential(self):
        """Abstract method to get the credential."""
        pass

    def __call__(self):
        """Allows the instance to be called like a function to get the credential."""
        return self.get_credential()