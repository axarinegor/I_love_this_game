from draw import Draw
from levels.level_1 import Level_1
from levels.level_4 import Level_4
from levels.level_2 import Level_2
from levels.level_3 import Level_3
from levels.level_8 import Level_8
from levels.level_7 import Level_7
from levels.level_12 import Level_12
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
        12: Level_12
    }

    @classmethod
    def create_level(cls, level_num: int, game_app: Any) -> LevelState:
        level_class = cls.LEVELS.get(level_num, Level_1)
        draw = Draw()
        physics = Physics(position=SPAWN_POSITION, width=40, height=68)
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