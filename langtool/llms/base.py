from abc import (
    abstractmethod,
    ABC,
)

class LLM(ABC):

    @abstractmethod
    def get_reply(self, message, **kwargs):
        pass