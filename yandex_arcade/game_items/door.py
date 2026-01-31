from dataclasses import dataclass

import arcade

from .. import protocols as proto
from ..tools.vector import Vector2, Vector2Int
from ..tools.physics import SHAPE, Physics, BLOCK_HEIGHT

@dataclass
class Door(proto.Door): 
    _physics: Physics
    _is_open: bool = False
    _color: arcade.color = (98, 181, 65)
    
    @property
    def physics(self) -> Physics:
        return self._physics
    
    @physics.setter
    def physics(self, value: Physics) -> None:
        self._physics = value
    
    @property
    def position(self) -> Vector2:
        return self._physics.position 
    
    def set_position(self, position: Vector2) -> None:
        self._physics.position = position
    
    @property
    def width(self) -> float:
        return self._physics.width
    
    def set_width(self, width: Vector2) -> None:
        self._physics.width = width
    
    @property
    def height(self) -> float:
        return self._physics.height
    
    def update(self, dt: float) -> None:
        if self._is_open:
            self._physics = Physics(_position=SHAPE.x - BLOCK_HEIGHT // 2, _width=BLOCK_HEIGHT, _height=100)
    
    def set_open(self, value: bool) -> None:
        self._is_open = value

    @property
    def is_open(self) -> bool:
        return self._is_open
    
    @is_open.setter
    def is_open(self, value: bool) -> None:
        self._is_open = value
    
    @property
    def color(self) -> arcade.color:
        return self._color
    
    @color.setter
    def color(self, value: arcade.color) -> None:
        self._color = value
