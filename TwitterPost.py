from abc import ABC,abstractmethod

class TwitterPost(ABC):
    @abstractmethod
    def get_post_text(self) -> str:
        pass
