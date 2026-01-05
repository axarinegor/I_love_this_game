from abc import ABC, abstractmethod
from typing import Callable
from physics import Physics
from vector import Vector2, Vector2Int
from dataclasses import dataclass




class Player(ABC):
    @property
    @abstractmethod
    def position(self) -> Vector2:
        ...
    
    @abstractmethod
    def set_direction(self, direction: Vector2) -> None:
        ...
    
    @abstractmethod
    def jump(self) -> None:
        ...
    
    @abstractmethod
    def update(self, dt: float, platforms: list = None) -> None:
        ...




class Platform(ABC):
    @abstractmethod
    def __post_init__(self):
        ...
    
    @property
    @abstractmethod
    def position(self) -> Vector2:
        ...
    
    @property
    @abstractmethod
    def width(self) -> float:
        ...
    
    @property
    @abstractmethod
    def height(self) -> float:
        ...
    
    @abstractmethod
    def update(self, dt: float) -> None:
        ...
    




class Door(ABC): 
    @property
    @abstractmethod
    def position(self) -> Vector2:
        ...
    
    @abstractmethod
    def set_position(self, position: Vector2) -> None:
        ...
    
    @property
    @abstractmethod
    def width(self) -> float:
        ...
    
    @abstractmethod
    def set_width(self, width: Vector2) -> None:
        ...
    
    @property
    @abstractmethod
    def height(self) -> float:
        ...
    
    @abstractmethod
    def update(self, dt: float) -> None:
        ...

    @abstractmethod
    def set_open(self, value: bool) -> None:
        ...

    @property
    @abstractmethod
    def get_open(self) -> bool:
        ...

class Rocket(ABC):
    @property
    @abstractmethod
    def physics(self) -> Physics:
        ...
    
    @abstractmethod
    def update(self, dt: float) -> None:
        ...

    @abstractmethod
    def touched(self, player) -> None:
        ...

class Rockets(ABC):
    @abstractmethod
    def spawn(self, position: Vector2) -> None:
        ...
 
    @abstractmethod
    def kill(self, rocket) -> None:
        ...

    @abstractmethod
    def apply(self, function) -> None:
        ...

    @abstractmethod
    def update(self, dt: float) -> None:
        ...

    @abstractmethod
    def touched(self, player):
        ...

    




'''
class Physics:
    @abstractmethod
    @property
    def bounds(self) -> tuple[float, float, float, float]:
        ...
    
    @abstractmethod
    @property
    def left(self) -> float:
        ...
    
    @abstractmethod
    @property
    def right(self) -> float:
        ...
    
    @abstractmethod
    @property
    def bottom(self) -> float:
        ...
    
    @abstractmethod
    @property
    def top(self) -> float:
        ...
    
    @abstractmethod
    def apply_force(self, force: Vector2) -> None:
        ...
    
    @abstractmethod
    def jump(self, jump_strength: float = None) -> bool:
        ...
    
    @abstractmethod
    def move(self, direction: Vector2, speed: float) -> None:
        ...
    
    @abstractmethod
    def update(self, dt: float) -> None:
        ...
    
    @abstractmethod
    def check_collision(self, other: 'Physics') -> tuple[bool, str, float]:
        ...
    
    @abstractmethod
    def resolve_collision(self, other: 'Physics', side: str, overlap: float) -> None:
        ...


'''