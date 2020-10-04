from abc import ABC, abstractmethod
from typing import Optional, Type, Callable, Dict


class LambdaHandler(ABC):

    @abstractmethod
    def handle(self, event: Optional[any]) -> Optional[any]:
        pass


def create_lambda_handler(
        lambda_handler: Type[LambdaHandler],
        dependencies: Optional[Dict[str, any]] = None
) -> Callable[[Optional[dict], Optional[any]], Optional[any]]:
    def __wrapped_handler(event: Optional[dict] = None, context: Optional[any] = None):
        return lambda_handler(**(dependencies or {})).handle(event)

    return __wrapped_handler
