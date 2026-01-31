import arcade
from yandex_arcade.protocols import Platform
from ..tools.physics import Physics
from ..tools.vector import Vector2


class Move:
    @staticmethod
    def keys_to_direction(keys: set[int]) -> Vector2:
        a_pressed = arcade.key.A in keys
        d_pressed = arcade.key.D in keys
        x = 0
        if d_pressed and not a_pressed:
            x = 1
        elif a_pressed and not d_pressed:
            x = -1
        
        return Vector2(x, 0)
    
    @staticmethod
    def should_jump(keys: set[int]) -> bool:
        return arcade.key.SPACE in keys
    
    def player_update(platforms: list[Platform] = None, physics: Physics = None) -> None:
        assert platforms
        
        player_corners = [
            Vector2(physics.left, physics.bottom),
            Vector2(physics.right, physics.bottom),
            Vector2(physics.left, physics.bottom + 1),
            Vector2(physics.right, physics.bottom + 1)
        ]
        
        is_on_platform = False
        
        for platform in platforms:
            temp_physics = Physics(
                _position=platform.position,
                _width=platform.width,
                _height=platform.height
            )
            
            has_collision, side, overlap = physics.check_collision(temp_physics)
            
            if has_collision:
                if side == 'top':
                    is_on_platform = True
                physics.resolve_collision(temp_physics, side, overlap)
                    
            for corner in player_corners:
                corner_physics = Physics(
                    _position=corner,
                    _width=1,
                    _height=1
                )
                corner_collision, corner_side, _ = corner_physics.check_collision(temp_physics)
                if corner_collision and corner_side == 'top':
                    is_on_platform = True
                    break

        physics.on_ground = is_on_platform