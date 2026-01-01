from digit_block import DIGIT_BLOCK_WIDTH, DigitBlock
from door import Door
from draw import PLAYER_SIZE, Draw
from gamerules import GameRules
from level_pattern import Lev_Patterns
from move import Move 
from observer import Event, OnEventSubscriber
from physics import BLOCK_HEIGHT, SHAPE, Physics
from texts import *
from vector import Vector2, Vector2Int
import protocols as proto
from typing import Any

class Level_15:
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 game_app: Any = None,
                 level_num: int = 4  
                 ) -> None:
        self._platforms = [i for i in Lev_Patterns.get_default(level_num)]
        self.background_color = (213, 255, 202)
        self.block_texture = Lev_Patterns.get_default_block()
        self._exit_position = Vector2(SHAPE.x - 15, BLOCK_HEIGHT + PLAYER_SIZE.y // 2)

        _pos_x = SHAPE.x - BLOCK_HEIGHT + 5
        _width = 10
        
        self.door_physics = Physics(position=Vector2(_pos_x, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=_width,
                                    height=PLAYER_SIZE.y + 16
                                )
        left_door_physics = Physics(position=Vector2(BLOCK_HEIGHT // 2, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 7),
                                    width=BLOCK_HEIGHT,
                                    height=PLAYER_SIZE.y + 16
                                )
        self._door = Door(physics=self.door_physics)
        self._left_door = Door(physics=left_door_physics, is_open=True)
        self._player = player
        self._draw = draw
        self.pressed_keys = set[int]()
        self.ANSWER = [5, 3, 9]
        
        self._keyboard_state_changed = Event[set[int], None]()
        self._keyboard_state_changed.subscribe(self._on_keys_changed)

        self.digit_blocks = []
        
        for i in range(3):
            block = DigitBlock(
                physics=Physics(
                    position=Vector2(410 + i * (DIGIT_BLOCK_WIDTH + 130), 400),
                    width=DIGIT_BLOCK_WIDTH,
                    height=DIGIT_BLOCK_WIDTH,
                    is_active=False
                )
            )
            self.digit_blocks.append(block)

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
            all_collision_objects = self._platforms + [self._door] + [i for i in self.digit_blocks]
            self._player.update(delta_time, all_collision_objects)
        else:
            self._player.update(delta_time, self._platforms + self.digit_blocks)
        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.complete_level(self.game_app, self.level_num)
        
        digs = [i.get_digit for i in self.digit_blocks]
        if digs == self.ANSWER:
            self.change_door(self._door, True)
            self._door.set_position(Vector2(SHAPE.x - BLOCK_HEIGHT // 2, self._door.position.y))
            self._door.set_width(BLOCK_HEIGHT)
        else:
            self.change_door(self._door, False)
            self._door.set_position(Vector2(SHAPE.x - BLOCK_HEIGHT + 5, self._door.position.y))
            self._door.set_width(10)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT:
            mouse_pos = Vector2(x, y)
            
            for block in self.digit_blocks:
                left = block.position.x - block.width/2
                right = block.position.x + block.width/2
                bottom = block.position.y - block.height/2
                top = block.position.y + block.height/2
                
                if left <= x <= right and bottom <= y <= top:
                    block.increment()
                    break

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

    def on_draw(self) -> None:
        arcade.set_background_color(self.background_color)
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self.block_texture)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        for block in self.digit_blocks:
            self._draw.digit_block(block)
        self._draw.texts(LEVEL_15)
    
    def change_door(self, door: Door, only: bool = None) -> None:
        if only is None:
            door.set_open(True if door.is_open == False else False)
            return
        door.set_open(only)