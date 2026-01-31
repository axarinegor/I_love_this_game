from dataclasses import dataclass, field
import os
from ..tools.vector import Vector2
import arcade
from ..patterns.texts import pixel_font
from ..tools.observer import Event
from ..other.sound_manager import background_music 


@dataclass
class Button:
    _text: str
    _position: Vector2
    _width: float = 200
    _height: float = 60
    _color: tuple[int, int, int] = (100, 100, 180)
    _text_color: tuple[int, int, int] = (255, 255, 255)
    _font_size: int = 24
    _kant_color: tuple[int, int, int] = (255, 255, 255)
    _text_obj: arcade.Text = None
    
    def __post_init__(self):
        self._text_obj = arcade.Text(
            text=self._text,
            x=self._position.x,
            y=self._position.y,
            color=self._text_color,
            font_size=self._font_size,
            anchor_x="center",
            anchor_y="center",
            font_name=pixel_font
        )
    
    def is_clicked(self, mouse_x: float, mouse_y: float) -> bool:
        left = self._position.x - self._width / 2
        right = self._position.x + self._width / 2
        bottom = self._position.y - self._height / 2
        top = self._position.y + self._height / 2
        clicked = left <= mouse_x <= right and bottom <= mouse_y <= top
        if clicked:
            parent_dir = os.path.dirname(os.path.dirname(__file__)) 
            music_path = os.path.join(parent_dir, "data", "click_music.mp3")
            background_music.play_sound_effect(music_path, volume=0.75)
        return clicked
    
    def draw(self) -> None:
        arcade.draw_lbwh_rectangle_filled(
            self._position.x - self._width // 2, self._position.y - self._height // 2,
            self._width, self._height,
            self._color
        )
        
        arcade.draw_lbwh_rectangle_outline(
            self._position.x - self._width // 2, self._position.y - self._height // 2,
            self._width, self._height,
            self._kant_color, 2
        )
        
        self._text_obj.draw()