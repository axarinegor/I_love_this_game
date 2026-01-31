from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Callable
from ..tools.physics import Physics
from .. import protocols as proto
import arcade
from ..tools.vector import Vector2, Vector2Int
from ..tools.physics import SHAPE

ROCKET_COLOR = arcade.color.SKOBELOFF
MAX_SPEED_ROCKET = 300

@dataclass
class Rocket(proto.Rocket):
    _position: Vector2
    _velocity: Vector2 = field(default_factory=lambda: Vector2(0, -1))
    _physics: Physics = field(default=None, init=False)

    def __post_init__(self):
        self._physics = Physics(
            _position=self._position,
            _width=50,
            _height=100,
            _gravity=800  
        )

    @property
    def position(self) -> Vector2:
        return self._position
    
    @position.setter
    def position(self, value: Vector2) -> None:
        self._position = value

    @property
    def physics(self) -> Physics:
        return self._physics

    @property
    def velocity(self) -> Vector2:
        return self._velocity
    
    @velocity.setter
    def velocity(self, value: Vector2) -> None:
        self._velocity = value

    def update(self, dt: float) -> None:
        self._physics.update(dt)
        self._position = self._physics.position
        if self._physics.position.y < -60:
            self._physics.position = Vector2(self._physics.position.x, 1000)
            self._physics.velocity = Vector2(0, 0)

    def touched(self, player: proto.Player) -> bool:
        px, py = player.position.x, player.position.y
        rx, ry = self.physics.position.x, self.physics.position.y
        return (px - player.width // 2 - 15 <= rx <= px + player.width // 2 + 15 and
                py - player.height // 2 - 40 <= ry <= py + player.height // 2 + 40)

@dataclass
class Rockets(proto.Rockets):
    _rockets: list[proto.Rocket]

    def spawn(self, position: Vector2) -> None:
        rocket = Rocket(_position=position)
        self._rockets.append(rocket)

    def kill(self, rocket: proto.Rocket) -> None:
        if rocket in self._rockets:
            return

    def apply(self, function: Callable[[proto.Rocket], None]) -> None:
        for rocket in self._rockets:
            function(rocket)

    def update(self, dt: float) -> None:
        for rocket in self._rockets:
            rocket.update(dt)

    def touched(self, player: proto.Player) -> bool:
        for rocket in self._rockets:
            if rocket.touched(player):
                self.kill(rocket) 
                return True
        return False

    def get(self) -> list[proto.Rocket]:
        return self._rockets