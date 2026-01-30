from typing import Any

from yandex_arcade.states.pause_menu import PauseMenu
from ..game_items.door import Door
from ..draw import PLAYER_SIZE, Draw
from ..other.gamerules import GameRules
from ..patterns.level_pattern import Lev_Patterns
from ..mover.move import Move
from ..tools.observer import Event, OnEventSubscriber
from ..tools.physics import BLOCK_HEIGHT, SHAPE, Physics
from ..patterns.texts import *
from ..tools.vector import Vector2, Vector2Int
from .. import protocols as proto
import arcade

class Level_3:
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 door_is_open: bool = True,
                 game_app: Any = None, 
                 level_num: int = 2    
                 ) -> None:
        self._background_color = (213, 255, 202)
        self._block_texture = Lev_Patterns.get_default_block()
        self._exit_position = Vector2(SHAPE.x - 15, BLOCK_HEIGHT + PLAYER_SIZE.y // 2)
        self._game_app = game_app
        self._level_num = level_num
        _pos_x = SHAPE.x - BLOCK_HEIGHT // 2
        _width = BLOCK_HEIGHT
        door_physics = Physics(_position=Vector2(_pos_x, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
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

    def _on_keys_changed(self, pressed_keys: set[int]) -> None:
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
        if not self._door.is_open:
            all_collision_objects = self._platforms + [self._door]
            self._player.update(delta_time, all_collision_objects)
            return
        self._player.update(delta_time, self._platforms)
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.complete_level(self._game_app, self._level_num)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
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
        arcade.draw_texture_rect(self._block_texture, arcade.XYWH(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT * 2.5, BLOCK_HEIGHT, BLOCK_HEIGHT))
        arcade.draw_texture_rect(self._block_texture, arcade.XYWH(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT * 3.5, BLOCK_HEIGHT, BLOCK_HEIGHT))
        arcade.draw_texture_rect(self._block_texture, arcade.XYWH(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT * 4.5, BLOCK_HEIGHT, BLOCK_HEIGHT))        
        self._draw.texts(LEVEL_3)