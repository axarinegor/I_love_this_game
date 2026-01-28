'''from animation import ExplosionEffect, RocketAnimation
from draw import Draw, PLAYER_SIZE
from texts import *
from level_pattern import Lev_Patterns, Rockets_8
from move import Move
from observer import Event, OnEventSubscriber
from physics import BLOCK_HEIGHT, SHAPE, SPAWN_POSITION, Physics
from vector import Vector2, Vector2Int
import protocols as proto
from door import Door
from gamerules import GameRules
from typing import Any

class Level_8:
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 door_is_open: bool = True,
                 game_app: Any = None, 
                 level_num: int = 8   
                 ) -> None:
        self.background_color = (213, 255, 202)
        self.block_texture = Lev_Patterns.get_default_block()
        self.rocket_texture = Lev_Patterns.get_default_rocket()
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
        self._rockets = Rockets_8
        self._explosion_effects = []
        self._player_exploded = False
        self._invulnerability_timer = 0.0
        self._invulnerability_duration = 1.0

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
        if self._invulnerability_timer > 0:
            self._invulnerability_timer -= delta_time
            if self._invulnerability_timer <= 0:
                self._invulnerability_timer = 0

        if self._player_exploded:
            for effect in self._explosion_effects[:]:
                effect.update(delta_time)
                if effect.is_finished():
                    self._explosion_effects.remove(effect)
            if not self._explosion_effects:
                self._player_exploded = False
                self.pressed_keys.clear()
                self._keyboard_state_changed.invoke(set())
                self.game_app.reset_level(self.level_num)
            return

        if not self._door.is_open:
            all_collision_objects = self._platforms + [self._door]
            self._player.update(delta_time, all_collision_objects)
            return
        self._player.update(delta_time, self._platforms)

        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.complete_level(self.game_app, self.level_num)

        self._rockets.update(delta_time)

        if self._rockets.touched(self._player):
            self._player_exploded = True
            explosion_pos = Vector2Int(int(self._player.position.x), int(self._player.position.y))
            self._explosion_effects.append(
                ExplosionEffect.create_at(
                    pos=explosion_pos,
                    anim_class=RocketAnimation,
                    folder='rocket_explode',
                    frames_count=7,
                    period=1.0,
                    pivot=Vector2Int(0, 0)
                )
            )

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.P:
            if not self.game_app.is_paused():
                self.game_app.pause_level()
            return
        if self._player_exploded:
            return
        if self._invulnerability_timer > 0:
            self.pressed_keys.clear()
            self._keyboard_state_changed.invoke(set())
            return
        self.pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        if self._invulnerability_timer > 0:
            return
        self.pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_draw(self) -> None:
        arcade.set_background_color(self.background_color)
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self.block_texture)
        for rocket in self._rockets.get():
            self._draw.rocket(rocket, self.rocket_texture)
        self._draw.explode(self._explosion_effects)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        self._draw.texts(LEVEL_8)

    def reset_level(self) -> None:
        self._player_exploded = False
        self._explosion_effects = []
        self._player.physics.position = SPAWN_POSITION
        self._player.physics.velocity = Vector2.zero()
        self.pressed_keys.clear()
        self._keyboard_state_changed.invoke(set())
        
    def on_mouse_press(self) -> None:
        return'''

from animation import ExplosionEffect, RocketAnimation
from draw import Draw, PLAYER_SIZE
from texts import *
from level_pattern import Lev_Patterns, Rockets_8
from move import Move
from observer import Event, OnEventSubscriber
from physics import BLOCK_HEIGHT, SHAPE, SPAWN_POSITION, Physics
from vector import Vector2, Vector2Int
import protocols as proto
from door import Door
from gamerules import GameRules
from typing import Any
import arcade

class Level_8:
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 door_is_open: bool = True,
                 game_app: Any = None, 
                 level_num: int = 8   
                 ) -> None:
        self._background_color = (213, 255, 202)
        self._block_texture = Lev_Patterns.get_default_block()
        self._rocket_texture = Lev_Patterns.get_default_rocket()
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
        self._rockets = Rockets_8
        self._explosion_effects = []
        self._player_exploded = False
        self._invulnerability_timer = 0.0
        self._invulnerability_duration = 1.0

        self._game_app = game_app
        self._level_num = level_num

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
    
    @property
    def rocket_texture(self) -> Any:
        return self._rocket_texture

    def on_fixed_update(self, delta_time: float) -> None:
        if self._invulnerability_timer > 0:
            self._invulnerability_timer -= delta_time
            if self._invulnerability_timer <= 0:
                self._invulnerability_timer = 0

        if self._player_exploded:
            for effect in self._explosion_effects[:]:
                effect.update(delta_time)
                if effect.is_finished():
                    self._explosion_effects.remove(effect)
            if not self._explosion_effects:
                self._player_exploded = False
                self._pressed_keys.clear()
                self._keyboard_state_changed.invoke(set())
                self._game_app.reset_level(self._level_num)
            return

        if not self._door.is_open:
            all_collision_objects = self._platforms + [self._door]
            self._player.update(delta_time, all_collision_objects)
            return
        self._player.update(delta_time, self._platforms)

        if GameRules.check_level_completion(self._player, self._exit_position):
            GameRules.complete_level(self._game_app, self._level_num)

        self._rockets.update(delta_time)

        if self._rockets.touched(self._player):
            self._player_exploded = True
            explosion_pos = Vector2Int(int(self._player.position.x), int(self._player.position.y))
            self._explosion_effects.append(
                ExplosionEffect.create_at(
                    pos=explosion_pos,
                    anim_class=RocketAnimation,
                    folder='rocket_explode',
                    frames_count=7,
                    period=1.0,
                    pivot=Vector2Int(0, 0)
                )
            )

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.ESCAPE:
            if not self._game_app.is_paused():
                self._game_app.pause_level()
            return
        if self._player_exploded:
            return
        if self._invulnerability_timer > 0:
            self._pressed_keys.clear()
            self._keyboard_state_changed.invoke(set())
            return
        self._pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self._pressed_keys)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        if self._invulnerability_timer > 0:
            return
        self._pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self._pressed_keys)

    def on_draw(self) -> None:
        arcade.set_background_color(self._background_color)
        self._draw.player(self._player)
        for platform in self._platforms:
            self._draw.platform(platform)
            self._draw.texture_wall(platform, self._block_texture)
        for rocket in self._rockets.get():
            self._draw.rocket(rocket, self._rocket_texture)
        self._draw.explode(self._explosion_effects)
        self._draw.door(self._door, Lev_Patterns.get_default_door())
        self._draw.door(self._left_door, Lev_Patterns.get_default_door())
        self._draw.texts(LEVEL_8)

    def reset_level(self) -> None:
        self._player_exploded = False
        self._explosion_effects = []
        self._player.physics.position = SPAWN_POSITION
        self._player.physics.velocity = Vector2.zero()
        self._pressed_keys.clear()
        self._keyboard_state_changed.invoke(set())
        
    def on_mouse_press(self) -> None:
        return