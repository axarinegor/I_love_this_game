'''from level_pattern import Lev_Patterns
from states.base_state import BaseState
from button import Button
import arcade
from dataclasses import dataclass
from texts import pixel_font
from vector import Vector2

@dataclass
class MainMenu(BaseState):
    width: int
    height: int
    title: arcade.Text = None
    buttons: list[Button] = None

    def __post_init__(self) -> None:
        self.title = arcade.Text(
            "I LOVE THIS GAME",
            self.width // 2, self.height - 130,
            arcade.color.BLACK, 28,
            anchor_x="center", anchor_y="center", font_name=pixel_font
        )
        self.buttons = [
            Button(text="Играть с начала", position=Vector2(self.width // 2, self.height // 2 + 80), kant_color=(0, 0, 0, 0), color=(0, 0, 0, 0), text_color=(0, 0, 0), font_size=16, width=400),
            Button(text="Уровни", position=Vector2(self.width // 2, self.height // 2 + 10), kant_color=(0, 0, 0, 0), color=(0, 0, 0, 0), text_color=(0, 0, 0), font_size=16),
            Button(text="Выход", position=Vector2(self.width // 2, self.height // 2 - 60), kant_color=(0, 0, 0, 0), color=(0, 0, 0, 0), text_color=(0, 0, 0), font_size=16)
        ]

    def handle_input(self, x: float = None, y: float = None, button: int = None, **kwargs) -> dict[str, any] | None:
        modifiers = kwargs.get('modifiers', 0)
        if x is not None and y is not None and button == arcade.MOUSE_BUTTON_LEFT:
            for i, btn in enumerate(self.buttons):
                if btn.is_clicked(x, y):
                    if i == 0:
                        return {"action": "reset_progress"}
                    elif i == 1:
                        return {"action": "open_level_select"}
                    elif i == 2:
                        return {"action": "exit"}
        return None

    def draw(self) -> None:
        intro = Lev_Patterns.get_intro_picture()
        arcade.draw_texture_rect(intro, arcade.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.title.draw()
        for btn in self.buttons:
            btn.draw()'''
from level_pattern import Lev_Patterns
from states.base_state import BaseState
from button import Button
import arcade
from dataclasses import dataclass
from texts import pixel_font
from vector import Vector2

@dataclass
class MainMenu(BaseState):
    _width: int
    _height: int
    _title: arcade.Text = None
    _buttons: list[Button] = None

    def __post_init__(self) -> None:
        self._title = arcade.Text(
            "I LOVE THIS GAME",
            self._width // 2, self._height - 130,
            arcade.color.BLACK, 28,
            anchor_x="center", anchor_y="center", font_name=pixel_font
        )
        self._buttons = [
            Button(_text="Играть с начала", _position=Vector2(self._width // 2, self._height // 2 + 80), _kant_color=(0, 0, 0, 0), _color=(0, 0, 0, 0), _text_color=(0, 0, 0), _font_size=16, _width=400, _height=60),
            Button(_text="Уровни", _position=Vector2(self._width // 2, self._height // 2 + 10), _kant_color=(0, 0, 0, 0), _color=(0, 0, 0, 0), _text_color=(0, 0, 0), _font_size=16, _width=200, _height=60),
            Button(_text="Выход", _position=Vector2(self._width // 2, self._height // 2 - 60), _kant_color=(0, 0, 0, 0), _color=(0, 0, 0, 0), _text_color=(0, 0, 0), _font_size=16, _width=200, _height=60)
        ]

    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    @property
    def title(self) -> arcade.Text:
        return self._title
    
    @property
    def buttons(self) -> list[Button]:
        return self._buttons

    def handle_input(self, x: float = None, y: float = None, button: int = None, **kwargs) -> dict[str, any] | None:
        _modifiers = kwargs.get('modifiers', 0)
        if x is not None and y is not None and button == arcade.MOUSE_BUTTON_LEFT:
            for i, btn in enumerate(self._buttons):
                if btn.is_clicked(x, y):
                    if i == 0:
                        return {"action": "reset_progress"}
                    elif i == 1:
                        return {"action": "open_level_select"}
                    elif i == 2:
                        return {"action": "exit"}
        return None

    def draw(self) -> None:
        _intro = Lev_Patterns.get_intro_picture()
        arcade.draw_texture_rect(_intro, arcade.XYWH(self._width // 2, self._height // 2, self._width, self._height))
        self._title.draw()
        for btn in self._buttons:
            btn.draw()