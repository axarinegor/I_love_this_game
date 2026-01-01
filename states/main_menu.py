from level_pattern import Lev_Patterns
from states.base_state import BaseState
from button import Button
import arcade
from dataclasses import dataclass
from typing import Optional, Any
from texts import BIG_SIZE, pixel_font
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
            btn.draw()