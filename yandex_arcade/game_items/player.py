from ..mover.move import Move
from ..tools.physics import Physics, SHAPE, SPAWN_POSITION
from ..mover.sprite import Sprite
from ..tools.vector import Vector2, Vector2Int
from dataclasses import dataclass, field
from .. import protocols as proto
from ..mover.animation import Animation


@dataclass
class Player(proto.Player):
    physics: Physics = field(default_factory=Physics)
    _speed: float = 150.0
    _walk_animation: Animation = field(default=None, init=False)
    _facing_right: bool = field(default=True, init=False)
    _is_moving: bool = field(default=False, init=False)
    _is_jumping: bool = field(default=False, init=False)
    _gravity_direction: int = 1 
    _stay_sprite: Sprite = field(default=None, init=False)
    _jump_sprites: Sprite = field(default=None, init=False)

    def __post_init__(self):
        self._walk_animation = Animation.load(frames_count=4, period=0.4)
        self._stay_sprite = Sprite.load_raw_image("stay.png", Vector2Int.zero())
        self._jump_sprites = Sprite.load_raw_image("jump.png", Vector2Int.zero())

    def set_direction(self, direction: Vector2) -> None:
        assert direction.length <= 1
        self.physics.move(direction, self._speed)
        self._is_moving = direction.x != 0
        if direction.x > 0:
            self._facing_right = True
        elif direction.x < 0:
            self._facing_right = False

    def update(self, dt: float, platforms: list[proto.Platform] = None) -> None:
        self.physics.update(dt, gravity_direction=self._gravity_direction)
        if platforms:
            Move.player_update(platforms, self.physics)
        if self.physics.on_ground:
            self._is_jumping = False
        self._walk_animation.update(dt) if not self._is_jumping and self._is_moving else self._walk_animation.reset()

    @property
    def texture(self):
        if self._is_moving and self._gravity_direction == -1:
            return self._walk_animation.current_frame.get()
        if self._is_jumping:
            return self._jump_sprites.get()
        return self._stay_sprite.get() if not self._is_moving else self._walk_animation.current_frame.get()

    @property
    def position(self) -> Vector2:
        return self.physics.position

    def jump(self) -> None:
        if self.physics.on_ground:
            self._is_jumping = True
            self._is_moving = False
            self.physics.jump()

    def toggle_gravity(self) -> None:
        self._gravity_direction *= -1

    @property
    def width(self) -> float:
        return self.physics.width

    @property
    def height(self) -> float:
        return self.physics.height

    @property
    def facing_right(self) -> bool:
        return self._facing_right

    @facing_right.setter
    def facing_right(self, value: bool) -> None:
        self._facing_right = value

    @property
    def gravity_direction(self) -> int:
        return self._gravity_direction

    @gravity_direction.setter
    def gravity_direction(self, value: int) -> None:
        self._gravity_direction = value