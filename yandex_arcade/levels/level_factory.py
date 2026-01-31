from ..draw import Draw
from .level_11 import Level_11
from .level_18 import Level_18
from .level_1 import Level_1
from .level_10 import Level_10
from .level_13 import Level_13
from .level_14 import Level_14
from .level_15 import Level_15
from .level_19 import Level_19
from .level_20 import Level_20
from .level_4 import Level_4
from .level_2 import Level_2
from .level_3 import Level_3
from .level_5 import Level_5
from .level_6 import Level_6
from .level_8 import Level_8
from .level_7 import Level_7
from .level_12 import Level_12
from .level_16 import Level_16
from .level_17 import Level_17
from .level_9 import Level_9
from ..tools.physics import SPAWN_POSITION, Physics
from ..game_items.player import Player 
from ..states.level import LevelState
from dataclasses import dataclass
from typing import Any
from ..tools.vector import Vector2Int

@dataclass
class LevelFactory:
    _LEVELS = {
        1: Level_1,
        2: Level_2,
        4: Level_4,
        7: Level_7,
        8: Level_8,
        3: Level_3,
        12: Level_12,
        16: Level_16,
        17: Level_17,
        6: Level_6,
        20: Level_20,
        19: Level_19,
        15: Level_15,
        14: Level_14,
        5: Level_5,
        18: Level_18,
        9: Level_9,
        13: Level_13,
        10: Level_10,
        11: Level_11
    }

    @classmethod
    def create_level(cls, level_num: int, game_app: Any) -> LevelState:
        level_class = cls._LEVELS.get(level_num, Level_1)
        draw = Draw()
        if level_num != 17:
            physics = Physics(_position=SPAWN_POSITION, _width=40, _height=68)
        else:
            physics = Physics(_position=SPAWN_POSITION, _width=40, _height=68, _gravity=-2600)
        player = Player(physics=physics, _speed=400)

        level_instance = level_class(
            title="Level",
            screen_shape=Vector2Int(1250, 650),
            draw=draw,
            player=player,
            game_app=game_app, 
            level_num=level_num 
        )
        return LevelState(_level_instance=level_instance, _game_app=game_app)