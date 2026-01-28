'''from dataclasses import dataclass
from vector import Vector2
import arcade
from texts import pixel_font

@dataclass
class Button:
    text: str
    position: Vector2
    width: float = 200
    height: float = 60
    color: tuple = (100, 100, 180)
    text_color: tuple = (255, 255, 255)
    font_size: int = 24
    kant_color: tuple = (255, 255, 255)
    
    def __post_init__(self):
        self.text_obj = arcade.Text(
            text=self.text,
            x=self.position.x,
            y=self.position.y,
            color=self.text_color,
            font_size=self.font_size,
            anchor_x="center",
            anchor_y="center",
            font_name=pixel_font
        )
    
    def is_clicked(self, mouse_x: float, mouse_y: float) -> bool:
        left = self.position.x - self.width / 2
        right = self.position.x + self.width / 2
        bottom = self.position.y - self.height / 2
        top = self.position.y + self.height / 2
        
        return left <= mouse_x <= right and bottom <= mouse_y <= top
    
    def draw(self) -> None:
        arcade.draw_lbwh_rectangle_filled(
            self.position.x - self.width // 2, self.position.y - self.height // 2,
            self.width, self.height,
            self.color
        )
        
        arcade.draw_lbwh_rectangle_outline(
            self.position.x - self.width // 2, self.position.y - self.height // 2,
            self.width, self.height,
            self.kant_color, 2
        )
        
        self.text_obj.draw()'''


from dataclasses import dataclass
from vector import Vector2
import arcade
from texts import pixel_font

@dataclass
class Button:
    _text: str
    _position: Vector2
    _width: float = 200
    _height: float = 60
    _color: tuple = (100, 100, 180)
    _text_color: tuple = (255, 255, 255)
    _font_size: int = 24
    _kant_color: tuple = (255, 255, 255)
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
        
        return left <= mouse_x <= right and bottom <= mouse_y <= top
    
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