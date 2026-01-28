'''from typing import Any
from level_pattern import Lev_Patterns
from states.base_state import BaseState
from button import Button
from vector import Vector2
import arcade
from dataclasses import dataclass
from texts import MEDIUM_SIZE, pixel_font

@dataclass
class LevelSelect(BaseState):
    width: int
    height: int
    save_system: Any 
    back_button: Button = None
    level_buttons: list[Button] = None

    def __post_init__(self) -> None:
        self.back_button = Button(
            text="Назад",
            position=Vector2(150, 90),
            width=120,
            height=40,
            font_size=18,
            color=(0, 0, 0, 0),
            text_color=(0, 0, 0),
            kant_color=(0, 0, 0, 0)
        )
        self.vibery_text = arcade.Text('Выбери уровень', 
                                       self.width // 2, 
                                       self.height - 90, 
                                       color=arcade.color.BLACK, 
                                       font_name=pixel_font, 
                                       font_size=MEDIUM_SIZE,
                                       anchor_x='center',
                                       anchor_y='center')
        self.level_buttons = self._create_level_buttons()

    def _create_level_buttons(self) -> list[Button]:
        buttons = []
        for level in range(1, 21):
            x = 330 + (level - 1) % 5 * 140
            y = self.height - 190 - (level - 1) // 5 * 120
            is_unlocked = self.save_system.is_level_unlocked(level)
            btn = Button(
                text=str(level) if is_unlocked else "?",
                position=Vector2(x, y),
                width=80,
                height=80,
                color=(100, 180, 100) if is_unlocked else (100, 100, 100), font_size=18
            )
            btn.level_num = level
            btn.is_unlocked = is_unlocked
            buttons.append(btn)
        return buttons

    def handle_input(self, x: float = None, y: float = None, button: int = None, **kwargs) -> dict[str, any] | None:
        modifiers = kwargs.get('modifiers', 0)
        if x is not None and y is not None and button == arcade.MOUSE_BUTTON_LEFT:
            if self.back_button.is_clicked(x, y):
                return {"action": "back"}
            for btn in self.level_buttons:
                if btn.is_clicked(x, y) and btn.is_unlocked:
                    return {"action": "start_game", "level_num": btn.level_num}
        return None

    def draw(self) -> None:
        intro = Lev_Patterns.get_level_picture()
        arcade.draw_texture_rect(intro, arcade.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.vibery_text.draw()
        self.back_button.draw()
        for btn in self.level_buttons:
            btn.draw()'''

from typing import Any
from level_pattern import Lev_Patterns
from states.base_state import BaseState
from button import Button
from vector import Vector2
import arcade
from dataclasses import dataclass
from texts import MEDIUM_SIZE, pixel_font

@dataclass
class LevelSelect(BaseState):
    _width: int
    _height: int
    _save_system: Any 
    _back_button: Button = None
    _level_buttons: list[Button] = None
    _vibery_text: arcade.Text = None

    def __post_init__(self) -> None:
        self._back_button = Button(
            _text="Назад",
            _position=Vector2(150, 90),
            _width=120,
            _height=40,
            _font_size=18,
            _color=(0, 0, 0, 0),
            _text_color=(0, 0, 0),
            _kant_color=(0, 0, 0, 0)
        )
        self._vibery_text = arcade.Text('Выбери уровень', 
                                       self._width // 2, 
                                       self._height - 90, 
                                       color=arcade.color.BLACK, 
                                       font_name=pixel_font, 
                                       font_size=MEDIUM_SIZE,
                                       anchor_x='center',
                                       anchor_y='center')
        self._level_buttons = self._create_level_buttons()

    def _create_level_buttons(self) -> list[Button]:
        buttons = []
        for level in range(1, 21):
            x = 330 + (level - 1) % 5 * 140
            y = self._height - 190 - (level - 1) // 5 * 120
            is_unlocked = self._save_system.is_level_unlocked(level)
            btn = Button(
                _text=str(level) if is_unlocked else "?",
                _position=Vector2(x, y),
                _width=80,
                _height=80,
                _color=(100, 180, 100) if is_unlocked else (100, 100, 100),
                _font_size=18
            )
            btn.level_num = level
            btn.is_unlocked = is_unlocked
            buttons.append(btn)
        return buttons

    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    @property
    def save_system(self) -> Any:
        return self._save_system
    
    @property
    def back_button(self) -> Button:
        return self._back_button
    
    @property
    def level_buttons(self) -> list[Button]:
        return self._level_buttons

    def handle_input(self, x: float = None, y: float = None, button: int = None, **kwargs) -> dict[str, any] | None:
        modifiers = kwargs.get('modifiers', 0)
        if x is not None and y is not None and button == arcade.MOUSE_BUTTON_LEFT:
            if self._back_button.is_clicked(x, y):
                return {"action": "back"}
            for btn in self._level_buttons:
                if btn.is_clicked(x, y) and btn.is_unlocked:
                    return {"action": "start_game", "level_num": btn.level_num}
        return None

    def draw(self) -> None:
        intro = Lev_Patterns.get_level_picture()
        arcade.draw_texture_rect(intro, arcade.XYWH(self._width // 2, self._height // 2, self._width, self._height))
        self._vibery_text.draw()
        self._back_button.draw()
        for btn in self._level_buttons:
            btn.draw()
