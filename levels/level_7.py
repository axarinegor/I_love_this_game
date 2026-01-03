from draw import Draw, PLAYER_SIZE
from texts import *
from level_pattern import Lev_Patterns
from move import Move 
from observer import Event, OnEventSubscriber
import arcade
from physics import BLOCK_HEIGHT, SHAPE, Physics
from vector import Vector2, Vector2Int
import protocols as proto
from door import Door
from gamerules import GameRules
from typing import Any

class Level_7:
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 door_is_open: bool = True,
                 game_app: Any = None,
                 level_num: int = 7     
                 ) -> None:
        self.background_color = (213, 255, 202)
        self.block_texture = Lev_Patterns.get_default_block()
        self._exit_position = Vector2(SHAPE.x - 15, BLOCK_HEIGHT + PLAYER_SIZE.y // 2)
        if not door_is_open:
            _pos_x = SHAPE.x - BLOCK_HEIGHT + 5
            _width = 10
        else:
            _pos_x = SHAPE.x - BLOCK_HEIGHT // 2
            _width = BLOCK_HEIGHT
        door_physics = Physics(position=Vector2(_pos_x, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=_width,
                                    height=PLAYER_SIZE.y + 16
                                )
        left_door_physics = Physics(position=Vector2(BLOCK_HEIGHT // 2, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=BLOCK_HEIGHT,
                                    height=PLAYER_SIZE.y + 16
                                )
        self._door = Door(physics=door_physics, is_open=door_is_open)
        self._left_door = Door(physics=left_door_physics, is_open=True)
        self._player = player
        self._draw = draw
        self.pressed_keys = set[int]()

        self._keyboard_state_changed = Event[set[int], None]()
        self._keyboard_state_changed.subscribe(self._on_keys_changed)

        self._platforms = [i for i in Lev_Patterns.get_default(level_num)]
        self.is_dark = False

        self.game_app = game_app
        self.level_num = level_num

    def _on_keys_changed(self, pressed_keys: set[int]) -> None:
        direction = Move.keys_to_direction(pressed_keys)
        self._player.set_direction(direction)
        if Move.should_jump(pressed_keys):
            self._player.jump()

    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber

    def on_fixed_update(self, delta_time: float) -> None:
        if not self._door.is_open:
            all_collision_objects = self._platforms + [self._door]
            self._player.update(delta_time, all_collision_objects)
            return
        self._player.update(delta_time, self._platforms)
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.complete_level(self.game_app, self.level_num)
        self.is_dark = self._player.physics.on_ground

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.P:
            if not self.game_app.is_paused():
                self.game_app.pause_level()
            return
        self.pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_mouse_press(self) -> None:
        return

    def on_draw(self) -> None:
        arcade.set_background_color(self.background_color)
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self.block_texture)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        self._draw.texts(LEVEL_7)
        if self.is_dark:
            arcade.draw_lbwh_rectangle_filled(
                0, 0,
                SHAPE.x, SHAPE.y, arcade.color.BLACK
            )