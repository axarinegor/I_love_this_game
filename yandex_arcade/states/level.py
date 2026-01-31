from .base_state import BaseState
import arcade
from dataclasses import dataclass
from typing import Any

@dataclass
class LevelState(BaseState):
    _level_instance: Any
    _game_app: Any
    _paused: bool = False
    _pause_menu: Any = None

    @property
    def level_instance(self) -> Any:
        return self._level_instance
    
    @property
    def game_app(self) -> Any:
        return self._game_app
    
    @property
    def paused(self) -> bool:
        return self._paused
    
    @paused.setter
    def paused(self, value: bool) -> None:
        self._paused = value
    
    @property
    def pause_menu(self) -> Any:
        return self._pause_menu
    
    @pause_menu.setter
    def pause_menu(self, value: Any) -> None:
        self._pause_menu = value

    def handle_input(self, x: float = None, y: float = None, button: int = None, **kwargs) -> None:
        if self._paused:
            action = self._pause_menu.handle_input(x, y, button, **kwargs)
            if action:
                self.handle_pause_action(action)
            return

        if 'key' in kwargs:
            key = kwargs['key']
            modifiers = kwargs.get('modifiers', 0)
            release = kwargs.get('release', False)
            if not release:
                self._level_instance.on_key_press(key, modifiers)
            else:
                self._level_instance.on_key_release(key, modifiers)
        if x is not None and y is not None and button is not None:
            modifiers = kwargs.get('modifiers', 0)
            self._level_instance.on_mouse_press(x, y, button, modifiers)
        elif x is not None and y is not None and button == arcade.MOUSE_BUTTON_LEFT:
            modifiers = kwargs.get('modifiers', 0)
            self._level_instance.on_mouse_press(x, y, button, modifiers)

    def handle_pause_action(self, action: dict[str, any]) -> None:
        if action["action"] == "resume":
            self._paused = False
            self._pause_menu = None
        elif action["action"] == "restart_level":
            level_num = action["level_num"]
            self._game_app.switch_to_state("level", level_num=level_num)
        elif action["action"] == "exit_to_menu":
            self._game_app.switch_to_state("main_menu")

    def update(self, delta_time: float) -> None:
        if not self._paused:
            self._level_instance.on_fixed_update(delta_time)

    def draw(self) -> None:
        self._level_instance.on_draw()
        if self._paused:
            self._pause_menu.draw()

    def toggle_pause(self) -> None:
        self._level_instance.pressed_keys.clear()
        self._level_instance._keyboard_state_changed.invoke(set())
        if not self._paused:
            from ..states.pause_menu import PauseMenu
            self._pause_menu = PauseMenu(
                _width=self._game_app.width,
                _height=self._game_app.height,
                _title="Уровень",
                _level_num=self._level_instance.level_num,
                _game_app_ref=self._game_app
            )
            self._paused = True
        else:
            self._level_instance.pressed_keys.clear()
            self._level_instance._keyboard_state_changed.invoke(set())
            self._paused = False
            self._pause_menu = None