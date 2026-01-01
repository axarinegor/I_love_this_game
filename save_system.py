import json
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Any

SAVE_FILE = "save_game.json"

@dataclass
class SaveSystem:
    save_path: Path = None
    data: Dict[str, Any] = None

    def __post_init__(self) -> None:
        self.save_path = Path(SAVE_FILE)
        self.data = self._load_or_create()

    def _load_or_create(self) -> Dict[str, Any]:
        if self.save_path.exists():
            with open(self.save_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return {
            "max_level_unlocked": 1,
            "completed_levels": []
        }

    def save(self) -> None:
        with open(self.save_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2)

    def unlock_level(self, level_num: int) -> None:
        if level_num > self.data["max_level_unlocked"]:
            self.data["max_level_unlocked"] = level_num
            self.save()

    def complete_level(self, level_num: int) -> None:
        if level_num not in self.data["completed_levels"]:
            self.data["completed_levels"].append(level_num)
            self.save()

    def is_level_unlocked(self, level_num: int) -> bool:
        return level_num <= self.data["max_level_unlocked"]

    def reset_progress(self) -> None:
        self.data = {
            "max_level_unlocked": 1,
            "completed_levels": []
        }
        self.save()

    def get_unlocked_levels_count(self) -> int:
        return self.data["max_level_unlocked"]