from draw import Draw
from levels.level_1 import Level_1
from levels.level_14 import Level_14
from levels.level_15 import Level_15
from levels.level_19 import Level_19
from levels.level_20 import Level_20
from levels.level_4 import Level_4
from levels.level_2 import Level_2
from levels.level_3 import Level_3
from levels.level_6 import Level_6
from levels.level_8 import Level_8
from levels.level_7 import Level_7
from levels.level_12 import Level_12
from levels.level_16 import Level_16
from levels.level_17 import Level_17
from physics import SPAWN_POSITION, Physics
from player import Player 
from states.level import LevelState
from dataclasses import dataclass
from typing import Any

from vector import Vector2Int

@dataclass
class LevelFactory:
    LEVELS = {
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
        14: Level_14
    }

    @classmethod
    def create_level(cls, level_num: int, game_app: Any) -> LevelState:
        level_class = cls.LEVELS.get(level_num, Level_1)
        draw = Draw()
        if level_num != 17:
            physics = Physics(position=SPAWN_POSITION, width=40, height=68)
        else:
            physics = Physics(position=SPAWN_POSITION, width=40, height=68, gravity=-2600)
        player = Player(physics=physics, _speed=400)

        level_instance = level_class(
            title="Level",
            screen_shape=Vector2Int(1250, 650),
            draw=draw,
            player=player,
            game_app=game_app, 
            level_num=level_num 
        )
        return LevelState(level_instance, game_app)