from states.base_state import BaseState
import arcade
from dataclasses import dataclass
from typing import Any

@dataclass
class LevelState(BaseState):
    level_instance: Any  # Level1, Level8, etc.
    game_app: Any  # GameApp
    paused: bool = False
    pause_menu: Any = None

    def handle_input(self, x: float = None, y: float = None, button: int = None, **kwargs) -> None:
        # Если пауза — передаём в меню
        if self.paused:
            action = self.pause_menu.handle_input(x, y, button, **kwargs)
            if action:
                self.handle_pause_action(action)
            return

        # Если не пауза — передаём в уровень
        if 'key' in kwargs:
            key = kwargs['key']
            modifiers = kwargs.get('modifiers', 0)
            release = kwargs.get('release', False)
            if not release:
                self.level_instance.on_key_press(key, modifiers)
            else:
                self.level_instance.on_key_release(key, modifiers)
        if x is not None and y is not None and button == arcade.MOUSE_BUTTON_LEFT:
            modifiers = kwargs.get('modifiers', 0)
            self.level_instance.on_mouse_press(x, y, button, modifiers)

    def handle_pause_action(self, action: dict[str, any]) -> None:
        if action["action"] == "resume":
            self.paused = False
            self.pause_menu = None
        elif action["action"] == "restart_level":
            level_num = action["level_num"]
            self.game_app.switch_to_state("level", level_num=level_num)
        elif action["action"] == "exit_to_menu":
            self.game_app.switch_to_state("main_menu")

    def update(self, delta_time: float) -> None:
        # Если не на паузе — обновляем уровень
        if not self.paused:
            self.level_instance.on_fixed_update(delta_time)

    def draw(self) -> None:
        self.level_instance.on_draw()
        if self.paused:
            self.pause_menu.draw()

    def toggle_pause(self) -> None:
        """Вызывается из уровня для переключения паузы."""
        self.level_instance.pressed_keys.clear()
        self.level_instance._keyboard_state_changed.invoke(set())
        if not self.paused:
            from states.pause_menu import PauseMenu
            self.pause_menu = PauseMenu(
                width=self.game_app.width,
                height=self.game_app.height,
                title="Уровень",
                level_num=self.level_instance.level_num,
                game_app_ref=self.game_app
            )
            self.paused = True
        else:
            self.level_instance.pressed_keys.clear()
            self.level_instance._keyboard_state_changed.invoke(set())
            self.paused = False
            self.pause_menu = None