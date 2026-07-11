from abc import ABC, abstractmethod

class BasePlugin(ABC):

    NAME="base"

    @abstractmethod
    def register(self):
        ...
