from dataclasses import dataclass, field
from .vector import Vector2, Vector2Int

JUMP_VELOCITY = 1100
SHAPE = Vector2Int(1250, 650)
SPAWN_POSITION = Vector2(90, 150)
BLOCK_HEIGHT = 50

@dataclass
class Physics:
    _position: Vector2 = field(default_factory=Vector2.zero)
    _velocity: Vector2 = field(default_factory=Vector2.zero)

    _width: float = 32.0
    _height: float = 48.0

    _on_ground: bool = False
    _is_active: bool = True

    _gravity: float = 2600.0
    _max_fall_speed: float = 1000.0

    @property
    def position(self) -> Vector2:
        return self._position
    
    @position.setter
    def position(self, value: Vector2) -> None:
        self._position = value
    
    @property
    def velocity(self) -> Vector2:
        return self._velocity
    
    @velocity.setter
    def velocity(self, value: Vector2) -> None:
        self._velocity = value
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: bool) -> None:
        self._width = value
    
    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, value: bool) -> None:
        self._height = value
    
    @property
    def on_ground(self) -> bool:
        return self._on_ground
    
    @on_ground.setter
    def on_ground(self, value: bool) -> None:
        self._on_ground = value
    
    @property
    def is_active(self) -> bool:
        return self._is_active
    
    @is_active.setter
    def is_active(self, value: bool) -> None:
        self._is_active = value
    
    @property
    def gravity(self) -> float:
        return self._gravity
    
    @property
    def max_fall_speed(self) -> float:
        return self._max_fall_speed

    @property
    def bounds(self) -> tuple[float, float, float, float]:
        return (
            self._position.x - self._width / 2,
            self._position.x + self._width / 2,
            self._position.y - self._height / 2,
            self._position.y + self._height / 2
        )

    @property
    def left(self) -> float:
        return self._position.x - self._width / 2

    @property
    def right(self) -> float:
        return self._position.x + self._width / 2

    @property
    def bottom(self) -> float:
        return self._position.y - self._height / 2

    @property
    def top(self) -> float:
        return self._position.y + self._height / 2

    def apply_force(self, force: Vector2) -> None:
        self._velocity += force

    def jump(self, jump_strength: float = JUMP_VELOCITY) -> bool:
        if self._on_ground and self._is_active:
            self._velocity = Vector2(self._velocity.x, jump_strength)
            self._on_ground = False
            return True
        return False

    def move(self, direction: Vector2, speed: float) -> None:
        if self._is_active:
            self._velocity = Vector2(direction.x * speed, self._velocity.y)

    def update(self, dt: float, gravity_direction: int = 1) -> None: 
        if not self._is_active:
            return

        self._velocity = Vector2(
            self._velocity.x,
            self._velocity.y - self._gravity * gravity_direction * dt  
        )

        if self._velocity.y < -self._max_fall_speed:
            self._velocity = Vector2(self._velocity.x, -self._max_fall_speed)

        self._position += self._velocity * dt
        if (self._position.y < -600) or (self._position.y > 1100):
            self._position = SPAWN_POSITION

    def check_collision(self, other: 'Physics') -> tuple[bool, str, float]:
        left1, right1, bottom1, top1 = self.bounds
        left2, right2, bottom2, top2 = other.bounds

        if not (right1 >= left2 and left1 <= right2 and
                top1 >= bottom2 and bottom1 <= top2):
            return False, "none", 0.0

        overlaps = {
            'left': right1 - left2,
            'right': right2 - left1,
            'top': top2 - bottom1,
            'bottom': top1 - bottom2
        }

        min_side = min(overlaps.items(), key=lambda x: x[1] if x[1] > 0 else float('inf'))

        return True, min_side[0], min_side[1]

    def resolve_collision(self, other: 'Physics', side: str, overlap: float) -> None:
        other_left, other_right, other_bottom, other_top = other.bounds

        if side == 'top':
            self._position = Vector2(
                self._position.x,
                other_top + self._height / 2 + 0.1 
            )
            if self._velocity.y < 0:
                self._velocity = Vector2(self._velocity.x, 0)
                self._on_ground = True

        elif side == 'left':
            self._position = Vector2(
                other_left - self._width / 2 - 0.1, 
                self._position.y
            )

        elif side == 'right':
            self._position = Vector2(
                other_right + self._width / 2 + 0.1,
                self._position.y
            )

        elif side == 'bottom':
            self._position = Vector2(
                self._position.x,
                other_bottom - self._height / 2 - 0.1 
            )
            if self._velocity.y > 0:
                self._velocity = Vector2(self._velocity.x, 0)