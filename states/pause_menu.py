from states.base_state import BaseState
from button import Button
from vector import Vector2
import arcade
from dataclasses import dataclass
from texts import pixel_font, NAME_LEVELS

@dataclass
class PauseMenu(BaseState):
    width: int
    height: int
    title: str
    level_num: int
    game_app_ref: any

    def __post_init__(self) -> None:
        self.title_text = arcade.Text(
            "ПАУЗА",
            self.width // 2, self.height - 200,
            arcade.color.WHITE, 23,
            anchor_x="center", anchor_y="center", font_name=pixel_font
        )
        self.level_text = arcade.Text(
            NAME_LEVELS[self.level_num],
            self.width // 2, self.height - 120,
            arcade.color.WHITE, 24,
            anchor_x="center", anchor_y="center", font_name=pixel_font
        )
        self.buttons = [
            Button("Продолжить", Vector2(self.width // 2, self.height // 2 + 80 - 10), font_size=20, color=(0, 0, 0, 0), width=300, kant_color=(0, 0, 0, 0)),
            Button("Начать заново", Vector2(self.width // 2, self.height // 2 - 10), font_size=20, color=(0, 0, 0, 0), width=360, kant_color=(0, 0, 0, 0)),
            Button("Выйти в меню", Vector2(self.width // 2, self.height // 2 - 80 - 10), font_size=20, color=(0, 0, 0, 0), width=360, kant_color=(0, 0, 0, 0))
        ]

    def handle_input(self, x: float = None, y: float = None, button: int = None, **kwargs) -> dict[str, any] | None:
        if x is not None and y is not None and button == arcade.MOUSE_BUTTON_LEFT:
            for i, btn in enumerate(self.buttons):
                if btn.is_clicked(x, y):
                    if i == 0:
                        return {"action": "resume"}
                    elif i == 1:
                        return {"action": "restart_level", "level_num": self.level_num}
                    elif i == 2:
                        return {"action": "exit_to_menu"}
        return None

    def draw(self) -> None:
        arcade.draw_rect_filled(arcade.XYWH(
            self.width // 2, self.height // 2, self.width, self.height),
            (0, 0, 0, 220)
        )
        self.level_text.draw()
        for btn in self.buttons:
            btn.draw()