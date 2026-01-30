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

class Level_5:
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 game_app: Any = None,
                 level_num: int = 5,
                 door_is_open: bool = False
                 ) -> None:
        self._background_color = (213, 255, 202)
        self._block_texture = Lev_Patterns.get_default_block()
        self._exit_position = Vector2(SHAPE.x - 15, BLOCK_HEIGHT + PLAYER_SIZE.y // 2)
        if not door_is_open:
            _pos_x = SHAPE.x - BLOCK_HEIGHT + 5
            _width = 10
        else:
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
        self._game_app = game_app
        self._level_num = level_num

        self._key_position = Vector2(150, SHAPE.y - BLOCK_HEIGHT * 2)
        self._key_texture = Lev_Patterns.get_key_texture()
        self._key_width, self._key_height = 80, 50
        self._key_taken = False

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
        if not self._key_taken:
            player_left = self._player.physics.position.x - self._player.physics.width / 2
            player_right = self._player.physics.position.x + self._player.physics.width / 2
            player_bottom = self._player.physics.position.y - self._player.physics.height / 2
            player_top = self._player.physics.position.y + self._player.physics.height / 2

            key_left = self._key_position.x - self._key_width / 2
            key_right = self._key_position.x + self._key_width / 2
            key_bottom = self._key_position.y - self._key_height / 2
            key_top = self._key_position.y + self._key_height / 2

            if (player_right > key_left and player_left < key_right and
                player_top > key_bottom and player_bottom < key_top):
                self._key_taken = True
                self.change_door(self._door, True)

        if not self._door.is_open:
            all_collision_objects = self._platforms + [self._door]
            self._player.update(delta_time, all_collision_objects)
            return
        self._player.update(delta_time, self._platforms)
        
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.complete_level(self._game_app, self._level_num)

    def change_door(self, door: Door, only: bool = None) -> None:
        if only is None:
            door.set_open(True if door.is_open == False else False)
            return
        door.set_open(True)
        door.set_position(Vector2(SHAPE.x - BLOCK_HEIGHT // 2, door.position.y))
        door.set_width(BLOCK_HEIGHT)
    
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self._pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self._pressed_keys)
        if PauseMenu.should_pause(self._pressed_keys, self._game_app.is_paused()):
            self._game_app.pause_level()

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self._pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self._pressed_keys)

    def on_mouse_press(self) -> None:
        return
    
    def on_draw(self) -> None:
        arcade.set_background_color(self._background_color)
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self._block_texture)
        if not self._key_taken:
            arcade.draw_texture_rect(self._key_texture, arcade.XYWH(
                self._key_position.x, self._key_position.y,
                self._key_width, self._key_height)
            )
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        self._draw.texts(LEVEL_5)