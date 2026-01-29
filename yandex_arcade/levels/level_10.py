from ..game_items.block import Platform
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

class Level_10:
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 game_app: Any = None,
                 level_num: int = 10,
                 door_is_open: bool = True
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

        self._chain_texture = Lev_Patterns.get_default_chain()
        self._blocks_chains = [
            Platform(_physics=Physics(
                _position=Vector2(300, 150),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(550, 350),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(850, 250),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            ))
            ]
        self._areas = [
            {"x": 0, "blocks": []}, 
            {"x": SHAPE.x // 3, "blocks": []}, 
            {"x": 2 * SHAPE.x // 3, "blocks": []},
        ]
        self._blocks_spawned = [False, False, False]

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
        all_collision_objects = self._platforms + ([self._door] if not self._door.is_open else [])
        for area in self._areas:
            all_collision_objects.extend(area["blocks"])
        self._player.update(delta_time, all_collision_objects)
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.complete_level(self._game_app, self._level_num)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button == arcade.MOUSE_BUTTON_MIDDLE:
            for i, area in enumerate(self._areas):
                left = area["x"]
                right = area["x"] + SHAPE.x // 3
                if left <= x <= right:
                    if not self._blocks_spawned[i]:
                        area = self._areas[i]
                        area["blocks"].append(self._blocks_chains[i])
                        self._blocks_spawned[i] = True

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.ESCAPE:
            if not self._game_app.is_paused():
                self._game_app.pause_level()
            return
        self._pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self._pressed_keys)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self._pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self._pressed_keys)

    def on_draw(self) -> None:
        arcade.set_background_color(self._background_color)
        self._draw.player(self._player)
        for area in self._areas:
            for block in area["blocks"]:
                self._draw.platform(block)
                self._draw.texture_wall(block, self._block_texture)
                self._draw.chain(block, self._chain_texture)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self._block_texture)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        self._draw.texts(LEVEL_10)