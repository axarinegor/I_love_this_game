from abc import abstractmethod
from dataclasses import dataclass
from ..tools.physics import Physics
from .. import protocols as proto
import arcade
from ..tools.vector import Vector2, Vector2Int

BLOCK_COLOR = arcade.color.SKOBELOFF

@dataclass
class Platform(proto.Platform):
    _physics: Physics
    _color: tuple = BLOCK_COLOR
    
    def __post_init__(self):
        self._physics.is_active = False
    
    @property
    def physics(self) -> Physics:
        return self._physics
    
    @physics.setter
    def physics(self, value: Physics) -> None:
        self._physics = value
    
    @property
    def color(self) -> tuple:
        return self._color
    
    @color.setter
    def color(self, value: tuple) -> None:
        self._color = value
    
    @property
    def position(self) -> Vector2:
        return self._physics.position
    
    @property
    def width(self) -> float:
        return self._physics.width
    
    @property
    def height(self) -> float:
        return self._physics.height
    
    def update(self, dt: float) -> None:
        if self._physics.is_active:
            self._physics.update(dt)