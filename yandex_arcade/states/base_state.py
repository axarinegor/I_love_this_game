from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class BaseState:
    def handle_input(self, *args: Any, **kwargs: Any) -> Optional[dict[str, Any]]:
        raise NotImplementedError

    def update(self, delta_time: float) -> None:
        pass

    def draw(self) -> None:
        raise NotImplementedError