from abc import ABC, abstractmethod

class BaseBuilder(ABC):

    NAME = "base"

    @abstractmethod
    def build(self):
        ...
