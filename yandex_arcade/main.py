import os
from pathlib import Path
import sys
import arcade
from .states.level import LevelState
from .states.main_menu import MainMenu
from .states.level_select import LevelSelect
from .levels.level_factory import LevelFactory
from .other.save_system import SaveSystem
from typing import Any
from .other.sound_manager import background_music


class GameApp(arcade.Window):
    def __init__(self) -> None:
        super().__init__(1250, 650, "I Love This Game", vsync=True)
        self._save_system = SaveSystem()
        self._state_stack = []
        self.push_state("main_menu")
        self.setup_background_music()

    def setup_background_music(self):
        #base_path = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parent))
        #music_path = base_path / "yandex_arcade" / "data" / "fon_music.mp3"
        background_music.load_and_play(Path('yandex_arcade/data/fon_music.mp3'), loop=True)


    @property
    def save_system(self) -> SaveSystem:
        return self._save_system
    
    @property
    def state_stack(self) -> list[LevelState]:
        return self._state_stack
    
    def push_state(self, state_name: str, **kwargs: Any) -> None:
        if state_name == "main_menu":
            state = MainMenu(self.width, self.height)
        elif state_name == "level_select":
            state = LevelSelect(self.width, self.height, self._save_system)
        elif state_name == "level":
            level_num = kwargs.get("level_num", 1)
            state = LevelFactory.create_level(level_num, self)
        else:
            return
        self._state_stack.append(state)

    def reset_level(self, level_num: int) -> None:
        if self._state_stack and isinstance(self._state_stack[-1], LevelState):
            self._state_stack.pop()
        self.push_state("level", level_num=level_num)
        
    def is_paused(self) -> bool:
        if self._state_stack and isinstance(self._state_stack[-1], LevelState):
            return self._state_stack[-1].paused
        return False

    def pause_level(self) -> None:
        if self._state_stack and isinstance(self._state_stack[-1], LevelState):
            self._state_stack[-1].toggle_pause()

    def pop_state(self) -> None:
        if len(self._state_stack) > 1:
            self._state_stack.pop()

    def switch_to_state(self, state_name: str, **kwargs: Any) -> None:
        self._state_stack = []
        self.push_state(state_name, **kwargs)

    def handle_action(self, action: dict[str, Any]) -> None:
        if action["action"] == "start_game":
            self.switch_to_state("level", level_num=action.get("level_num", 1))
        elif action["action"] == "open_level_select":
            self.push_state("level_select")
        elif action["action"] == "back":
            self.pop_state()
        elif action["action"] == "exit":
            arcade.close_window()
        elif action["action"] == "reset_progress":
            self._save_system.reset_progress()
            self.switch_to_state("level", level_num=1)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if self._state_stack:
            action = self._state_stack[-1].handle_input(x, y, button, modifiers=modifiers)
            if action:
                self.handle_action(action)

    def on_key_press(self, key: int, modifiers: int) -> None:
        if self._state_stack:
            self._state_stack[-1].handle_input(key=key, modifiers=modifiers)

    def on_key_release(self, key: int, modifiers: int) -> None:
        if self._state_stack:
            self._state_stack[-1].handle_input(key=key, modifiers=modifiers, release=True)

    def on_update(self, delta_time: float) -> None:
        if self._state_stack:
            self._state_stack[-1].update(delta_time)

    def on_draw(self) -> None:
        self.clear()
        if self._state_stack:
            self._state_stack[-1].draw()


def main() -> None:
    game = GameApp()
    arcade.run()

if __name__ == "__main__":
    main()