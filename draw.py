'''import pyglet
from digit_block import DigitBlock
from physics import BLOCK_HEIGHT
from rocket import Rocket
from vector import Vector2Int
import arcade
from dataclasses import dataclass
import protocols as proto


PLAYER_SIZE = Vector2Int(40, 68)
PLAYER_COLOR = arcade.color.SILVER_CHALICE
PLAYER_BORDER_COLOR = arcade.color.BLACK


@dataclass
class Draw:
    def player(self, player: proto.Player, is_normal: int = 1) -> None:
        if not player.facing_right:
            arcade.draw_texture_rect(
                texture=player.texture,
                rect=arcade.rect.XYWH(x=player.position.x,
                                    y=player.position.y,
                                    width=-player.width,
                                    height=is_normal * player.height))
        else:
            arcade.draw_texture_rect(
                texture=player.texture,
                rect=arcade.rect.XYWH(x=player.position.x,
                                    y=player.position.y,
                                    width=player.width,
                                    height=is_normal * player.height))

    def platform(self, platform: proto.Platform) -> None:
        arcade.draw_lbwh_rectangle_filled(
            left=platform.position.x - platform.width // 2,
            bottom=platform.position.y - platform.height // 2,
            width=platform.width,
            height=platform.height,
            color=(84, 135, 37)
        )

    def door(self, door: proto.Door, texture) -> None:
        if door.get_open:
            arcade.draw_texture_rect(
                    texture=texture,
                    rect=arcade.rect.LBWH(left=door.position.x - door.width // 2, 
                                        bottom=door.position.y - door.height // 2, 
                                        width=door.width, 
                                        height=door.height)
                )
        else:    
            arcade.draw_lbwh_rectangle_filled(
                left=door.position.x - door.width // 2,
                bottom=door.position.y - door.height // 2,
                width=door.width,
                height=door.height,
                color=door.color
            )

    def chain(self, platform: proto.Platform, texture) -> None:
        arcade.draw_texture_rect(
                    texture=texture,
                    rect=arcade.rect.LBWH(left=platform.position.x - 55, 
                                        bottom=platform.position.y + platform.height // 2, 
                                        width=100, 
                                        height=500)
                )

    def texture_wall(self, platform: proto.Platform, texture: arcade.Texture) -> None:
        tiles_y_count = int(platform.height / BLOCK_HEIGHT)
        tiles_x_count = int(platform.width / BLOCK_HEIGHT)
        
        start_x = platform.position.x - platform.width / 2 + BLOCK_HEIGHT / 2
        start_y = platform.position.y - platform.height / 2 + BLOCK_HEIGHT / 2
    
        for j in range(tiles_x_count):
            for i in range(tiles_y_count):
                pos_x = start_x + j * BLOCK_HEIGHT
                pos_y = start_y + i * BLOCK_HEIGHT
                arcade.draw_texture_rect(
                    texture=texture,
                    rect=arcade.rect.XYWH(x=pos_x, 
                                        y=pos_y, 
                                        width=BLOCK_HEIGHT, 
                                        height=BLOCK_HEIGHT)
                )

    def texts(self, texts: list[arcade.Text]) -> None:
        for text in texts:
            text.draw()

    def digit_block(self, block: DigitBlock) -> None:
        arcade.draw_lbwh_rectangle_filled(
            block.position.x - block.width // 2, 
            block.position.y - block.height // 2,
            block.width, block.height,
            block.color
        )
        arcade.draw_lbwh_rectangle_outline(
            block.position.x - block.width // 2, 
            block.position.y - block.height // 2,
            block.width, block.height,
            (98, 181, 65), 3
        )
        
        block.to_draw().draw()

    def rocket(self, rocket: Rocket, texture: arcade.Texture) -> None:
        arcade.draw_texture_rect(
                    texture=texture,
                    rect=arcade.rect.XYWH(x=rocket.position.x, 
                                        y=rocket.position.y, 
                                        width=rocket.physics.width, 
                                        height=rocket.physics.height)
                )

    def explode(self, explosion_effects: list):
        if not explosion_effects:
            return
        for effect in explosion_effects:
            arcade.draw_texture_rect(
                texture=effect.get_texture(),
                rect=arcade.rect.XYWH(
                    x=effect.get_position().x,
                    y=effect.get_position().y,
                    width=64,
                    height=64
                )
            )

    def level_4(self) -> None:
        color = (77, 123, 34)
        arcade.draw_triangle_outline(470, 150, 520, 150, 495, 200, color, 4)
        arcade.draw_circle_outline(590, 172, 30, color, 4)
        arcade.draw_lbwh_rectangle_outline(670, 140, 50, 60, color, 4)

    def pause(width, height, buttons, level_text) -> None:
        arcade.draw_rect_filled(arcade.XYWH(
            width // 2, height // 2, width, height),
            (0, 0, 0, 220)
        )
        level_text.draw()
        for btn in buttons:
            btn.draw()

            

'''
import pyglet
from digit_block import DigitBlock
from physics import BLOCK_HEIGHT
from rocket import Rocket
from vector import Vector2Int
import arcade
from dataclasses import dataclass
import protocols as proto


PLAYER_SIZE = Vector2Int(40, 68)
PLAYER_COLOR = arcade.color.SILVER_CHALICE
PLAYER_BORDER_COLOR = arcade.color.BLACK


@dataclass
class Draw:
    def player(self, player: proto.Player, is_normal: int = 1) -> None:
        if not player.facing_right:
            arcade.draw_texture_rect(
                texture=player.texture,
                rect=arcade.rect.XYWH(x=player.position.x,
                                    y=player.position.y,
                                    width=-player.width,
                                    height=is_normal * player.height))
        else:
            arcade.draw_texture_rect(
                texture=player.texture,
                rect=arcade.rect.XYWH(x=player.position.x,
                                    y=player.position.y,
                                    width=player.width,
                                    height=is_normal * player.height))

    def platform(self, platform: proto.Platform) -> None:
        arcade.draw_lbwh_rectangle_filled(
            left=platform.position.x - platform.width // 2,
            bottom=platform.position.y - platform.height // 2,
            width=platform.width,
            height=platform.height,
            color=(84, 135, 37)
        )

    def door(self, door: proto.Door, texture) -> None:
        if door.is_open:
            arcade.draw_texture_rect(
                    texture=texture,
                    rect=arcade.rect.LBWH(left=door.position.x - door.width // 2, 
                                        bottom=door.position.y - door.height // 2, 
                                        width=door.width, 
                                        height=door.height)
                )
        else:    
            arcade.draw_lbwh_rectangle_filled(
                left=door.position.x - door.width // 2,
                bottom=door.position.y - door.height // 2,
                width=door.width,
                height=door.height,
                color=door.color
            )

    def chain(self, platform: proto.Platform, texture) -> None:
        arcade.draw_texture_rect(
                    texture=texture,
                    rect=arcade.rect.LBWH(left=platform.position.x - 55, 
                                        bottom=platform.position.y + platform.height // 2, 
                                        width=100, 
                                        height=500)
                )

    def texture_wall(self, platform: proto.Platform, texture: arcade.Texture) -> None:
        tiles_y_count = int(platform.height / BLOCK_HEIGHT)
        tiles_x_count = int(platform.width / BLOCK_HEIGHT)
        
        _start_x = platform.position.x - platform.width / 2 + BLOCK_HEIGHT / 2
        _start_y = platform.position.y - platform.height / 2 + BLOCK_HEIGHT / 2
    
        for j in range(tiles_x_count):
            for i in range(tiles_y_count):
                _pos_x = _start_x + j * BLOCK_HEIGHT
                _pos_y = _start_y + i * BLOCK_HEIGHT
                arcade.draw_texture_rect(
                    texture=texture,
                    rect=arcade.rect.XYWH(x=_pos_x, 
                                        y=_pos_y, 
                                        width=BLOCK_HEIGHT, 
                                        height=BLOCK_HEIGHT)
                )

    def texts(self, texts: list[arcade.Text]) -> None:
        for text in texts:
            text.draw()

    def digit_block(self, block: DigitBlock) -> None:
        arcade.draw_lbwh_rectangle_filled(
            block.position.x - block.width // 2, 
            block.position.y - block.height // 2,
            block.width, block.height,
            block.color
        )
        arcade.draw_lbwh_rectangle_outline(
            block.position.x - block.width // 2, 
            block.position.y - block.height // 2,
            block.width, block.height,
            (98, 181, 65), 3
        )
        
        block.to_draw().draw()

    def rocket(self, rocket: Rocket, texture: arcade.Texture) -> None:
        arcade.draw_texture_rect(
                    texture=texture,
                    rect=arcade.rect.XYWH(x=rocket.position.x, 
                                        y=rocket.position.y, 
                                        width=rocket.physics.width, 
                                        height=rocket.physics.height)
                )

    def explode(self, explosion_effects: list):
        if not explosion_effects:
            return
        for effect in explosion_effects:
            arcade.draw_texture_rect(
                texture=effect.get_texture(),
                rect=arcade.rect.XYWH(
                    x=effect.get_position().x,
                    y=effect.get_position().y,
                    width=64,
                    height=64
                )
            )

    def level_4(self) -> None:
        _color = (77, 123, 34)
        arcade.draw_triangle_outline(470, 150, 520, 150, 495, 200, _color, 4)
        arcade.draw_circle_outline(590, 172, 30, _color, 4)
        arcade.draw_lbwh_rectangle_outline(670, 140, 50, 60, _color, 4)

    def pause(width, height, buttons, level_text) -> None:
        arcade.draw_rect_filled(arcade.XYWH(
            width // 2, height // 2, width, height),
            (0, 0, 0, 220)
        )
        level_text.draw()
        for btn in buttons:
            btn.draw()