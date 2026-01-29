from dataclasses import dataclass
from ..tools.physics import Physics
from ..tools.vector import Vector2
import arcade
from .. import protocols as proto
from ..patterns.texts import pixel_font

DIGIT_BLOCK_WIDTH = 65

@dataclass
class DigitBlock(proto.Platform):
    _physics: Physics
    _current_digit: int = 0 
    _color: tuple = (213, 255, 202) 
    _text_color: tuple = (0, 0, 0)
    _font_size: int = DIGIT_BLOCK_WIDTH // 3
    _text_obj: arcade.Text = None
    
    def __post_init__(self):
        self._physics.is_active = False
        self._text_obj = arcade.Text(
            str(self._current_digit),
            self.position.x, self.position.y,
            self._text_color, self._font_size,
            align="center", anchor_x="center", anchor_y="center",
            font_name=pixel_font, bold=True
        )
    
    @property
    def physics(self) -> Physics:
        return self._physics
    
    @property
    def position(self) -> Vector2:
        return self._physics.position
    
    @property
    def width(self) -> float:
        return self._physics.width
    
    @property
    def height(self) -> float:
        return self._physics.height
    
    @property
    def current_digit(self) -> int:
        return self._current_digit
    
    @property
    def color(self) -> tuple:
        return self._color
    
    @property
    def text_color(self) -> tuple:
        return self._text_color
    
    @property
    def font_size(self) -> int:
        return self._font_size
    
    @property
    def text_obj(self) -> arcade.Text:
        return self._text_obj

    def update(self, dt: float) -> None:
        pass
    
    def increment(self) -> None:
        self._current_digit = (self._current_digit + 1) % 10
        self._text_obj.text = str(self._current_digit)
    
    def decrement(self) -> None:
        self._current_digit = (self._current_digit - 1) % 10
        self._text_obj.text = str(self._current_digit)
    
    def set_digit(self, digit: int) -> None:
        self._current_digit = max(0, min(9, digit))
        self._text_obj.text = str(self._current_digit)
    
    def to_draw(self) -> arcade.Text:
        return self._text_obj
    
    @property
    def get_digit(self) -> int:
        return self._current_digit
    

@dataclass
class LetterBlock:
    _physics: Physics
    _letter: str = 'A'
    _color: tuple = (213, 255, 202)
    _text_color: tuple = (0, 0, 0)
    _font_size: int = DIGIT_BLOCK_WIDTH // 3
    _text: arcade.Text = None

    def __post_init__(self):
        self._text = arcade.Text(
                text="A",
                x=self._physics.position.x,
                y=self._physics.position.y,
                color=(255, 255, 255),
                font_size=self._font_size,
                anchor_x="center",
                anchor_y="center",
                bold=True
            )
    
    @property
    def physics(self) -> Physics:
        return self._physics
    
    @property
    def position(self) -> Vector2:
        return self._physics.position
    
    @property
    def width(self) -> float:
        return self._physics.width
    
    @property
    def height(self) -> float:
        return self._physics.height
    
    @property
    def letter(self) -> str:
        return self._letter
    
    @property
    def color(self) -> tuple:
        return self._color
    
    @property
    def text_color(self) -> tuple:
        return self._text_color
    
    @property
    def font_size(self) -> int:
        return self._font_size
    
    @property
    def text(self) -> arcade.Text:
        return self._text

    def is_clicked(self, mouse_x, mouse_y):
        left = self._physics.left
        right = self._physics.right
        bottom = self._physics.bottom
        top = self._physics.top
        
        return (left <= mouse_x <= right and bottom <= mouse_y <= top)
    
    def increment(self):
        current_ord = ord(self._letter)
        if current_ord == ord('Z'):
            self._letter = 'A'
        else:
            self._letter = chr(current_ord + 1)
        self._text.text = self._letter
    
    @property
    def get_digit(self) -> str:
        return self._letter
    
    def to_draw(self) -> arcade.Text:
        return arcade.Text(
            str(self._letter),
            self.position.x, self.position.y,
            self._text_color, self._font_size,
            align="center", anchor_x="center", anchor_y="center",
            font_name=pixel_font, bold=True
        )