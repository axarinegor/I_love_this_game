from yandex_arcade.states.pause_menu import PauseMenu
from ..draw import Draw, PLAYER_SIZE
from ..patterns.texts import *
from ..patterns.level_pattern import Lev_Patterns
from ..mover.move import Move
from ..tools.observer import Event, OnEventSubscriber
import arcade
from ..tools.physics import BLOCK_HEIGHT, SHAPE, Physics
from ..tools.vector import Vector2, Vector2Int
from .. import protocols as proto
from ..game_items.door import Door
from ..other.gamerules import GameRules
from typing import Any

class Level_18:
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 game_app: Any = None,
                 level_num: int = 18,
                 door_is_open: bool = True
                 ) -> None:
        self._background_color = (213, 255, 202)
        self._exit_position = Vector2(BLOCK_HEIGHT // 2, SHAPE.y - 180)
        self._block_texture = Lev_Patterns.get_default_block()
        if not door_is_open:
            _pos_x = BLOCK_HEIGHT + 5
            _width = 10
        else:
            _pos_x = BLOCK_HEIGHT // 2
            _width = BLOCK_HEIGHT
        door_physics = Physics(_position=Vector2(_pos_x, SHAPE.y - 182),
                                    _width=_width,
                                    _height=PLAYER_SIZE.y + 16
                                )
        left_door_physics = Physics(_position=Vector2(BLOCK_HEIGHT // 2, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    _width=BLOCK_HEIGHT,
                                    _height=PLAYER_SIZE.y + 16
                                )
        self._door = Door(_physics=door_physics, _is_open=door_is_open)
        self._left_door = Door(_physics=left_door_physics, _is_open=True)
        self._player = player
        self._draw = draw
        self._pressed_keys = set[int]()

        self._keyboard_state_changed = Event[set[int], None]()
        self._keyboard_state_changed.subscribe(self._on_keys_changed)

        self._platforms = [i for i in Lev_Patterns.get_default(level_num)]
        self._game_app = game_app
        self._level_num = level_num

        self._left_mouse_pressed = False
        self._freeze_y = 0
        self._is_frozen = False

    def _on_keys_changed(self, pressed_keys: set[int]) -> None:
        if self._left_mouse_pressed:
            direction = Move.keys_to_direction(pressed_keys)
            self._player.set_direction(Vector2(direction.x, 0))
        else:
            direction = Move.keys_to_direction(pressed_keys)
            self._player.set_direction(direction)
            if Move.should_jump(pressed_keys):
                self._player.jump()

    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber

    @property
    def game_app(self) -> Any:
        return self._game_app
    
    @property
    def level_num(self) -> int:
        return self._level_num
    
    @property
    def pressed_keys(self) -> set[int]:
        return self._pressed_keys
    
    @property
    def background_color(self) -> tuple:
        return self._background_color
    
    @property
    def block_texture(self) -> Any:
        return self._block_texture

    def on_fixed_update(self, delta_time: float) -> None:
        if self._left_mouse_pressed:
            if not self._is_frozen:
                self._freeze_y = self._player.physics.position.y
                self._is_frozen = True
            
            original_velocity = self._player.physics.velocity
            
            self._player.physics.velocity = Vector2(original_velocity.x, 0)
            self._player.physics.on_ground = False
            
            if not self._door.is_open:
                all_collision_objects = self._platforms + [self._door]
                self._player.update(delta_time, all_collision_objects)
            else:
                self._player.update(delta_time, self._platforms)
            
            self._player.physics.position = Vector2(
                self._player.physics.position.x,
                self._freeze_y
            )
            
        else:
            if self._is_frozen:
                self._is_frozen = False
            
            if not self._door.is_open:
                all_collision_objects = self._platforms + [self._door]
                self._player.update(delta_time, all_collision_objects)
            else:
                self._player.update(delta_time, self._platforms)
        
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.complete_level(self._game_app, self._level_num)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT:
            self._left_mouse_pressed = not self._left_mouse_pressed
            self._keyboard_state_changed.invoke(self._pressed_keys)
            return

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self._pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self._pressed_keys)
        if PauseMenu.should_pause(self._pressed_keys, self._game_app.is_paused()):
            self._game_app.pause_level()

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self._pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self._pressed_keys)

    def on_draw(self) -> None:
        arcade.set_background_color(self._background_color)
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self._block_texture)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        self._draw.texts(LEVEL_18)