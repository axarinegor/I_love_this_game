from dataclasses import dataclass
from pathlib import Path
import arcade
from block import Platform
from draw import PLAYER_SIZE
from rocket import Rocket, Rockets
from vector import Vector2
from physics import Physics, SHAPE, BLOCK_HEIGHT

default_pattern_1 = [
            Platform(physics=Physics(
                position=Vector2(200, BLOCK_HEIGHT // 2),
                width=400,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 200, BLOCK_HEIGHT // 2),
                width=400,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(500, 200),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(700, 200),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(2, BLOCK_HEIGHT * 2),
                width=4,
                height=PLAYER_SIZE.y + 16
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                width=2,
                height=PLAYER_SIZE.y + 16),
                color=arcade.color.CARIBBEAN_GREEN
            )
        ]


@dataclass
class Lev_Patterns:
    def get_default(x: int = 1) -> list[Platform]:
        patterns = {
            1: default_pattern_1,
            2: default_pattern_2,
            4: default_pattern_4,
            6: default_pattern_6,
            12: default_pattern_12,
            7: default_pattern_7,
            3: default_pattern_3,
            8: default_pattern_8
        }
        
        return patterns.get(x, default_pattern_1)
    
    def get_default_block() -> arcade.Texture:
        texture_path = Path("data/block.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_default_door() -> arcade.Texture:
        texture_path = Path("data/door.jpg")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_default_rocket() -> arcade.Texture:
        texture_path = Path("data/rocket.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_intro_picture() -> arcade.Texture:
        texture_path = Path("data/intro.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_level_picture() -> arcade.Texture:
        texture_path = Path("data/level_select.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)

default_pattern_2 = [
            Platform(physics=Physics(
                position=Vector2(200, BLOCK_HEIGHT // 2),
                width=400,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 200, BLOCK_HEIGHT // 2),
                width=400,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(800, -100),
                width=500,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(2, BLOCK_HEIGHT * 2),
                width=4,
                height=PLAYER_SIZE.y + 16
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                width=2,
                height=PLAYER_SIZE.y + 16),
                color=arcade.color.CARIBBEAN_GREEN
            )
        ]

default_pattern_3 = [
            Platform(physics=Physics(
                position=Vector2(200, BLOCK_HEIGHT // 2),
                width=400,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(-2, SHAPE.y // 2),
                width=4,
                height=SHAPE.y
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 200, BLOCK_HEIGHT // 2),
                width=400,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT * 3 + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT * 5
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT * 1.5),
                width=BLOCK_HEIGHT,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(550, 370),
                width=600,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(2, BLOCK_HEIGHT * 2),
                width=4,
                height=PLAYER_SIZE.y + 16
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                width=2,
                height=PLAYER_SIZE.y + 16),
                color=arcade.color.CARIBBEAN_GREEN
            )
        ]

default_pattern_4 = [
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(2, BLOCK_HEIGHT * 2),
                width=4,
                height=PLAYER_SIZE.y + 16
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                width=2,
                height=PLAYER_SIZE.y + 16),
                color=arcade.color.CARIBBEAN_GREEN
            ),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2 - 25, 300),
                width=450,
                height=BLOCK_HEIGHT)
            ),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2 - 340, 150),
                width=BLOCK_HEIGHT,
                height=BLOCK_HEIGHT)
            ),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2 + 340, 150),
                width=BLOCK_HEIGHT,
                height=BLOCK_HEIGHT)
            ),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2 - 225, 150),
                width=BLOCK_HEIGHT,
                height=300)
            ),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2 + 175, 150),
                width=BLOCK_HEIGHT,
                height=300)
            )
        ]


default_pattern_6 = [
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(2, BLOCK_HEIGHT * 2),
                width=4,
                height=PLAYER_SIZE.y + 16
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                width=2,
                height=PLAYER_SIZE.y + 16),
                color=arcade.color.CARIBBEAN_GREEN
            )
        ]

default_pattern_12 = [
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(2, BLOCK_HEIGHT * 2),
                width=4,
                height=PLAYER_SIZE.y + 16
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                width=2,
                height=PLAYER_SIZE.y + 16),
                color=arcade.color.CARIBBEAN_GREEN)
        ]

Rockets_8 = Rockets([Rocket(position=Vector2(150, 1050)),
                     Rocket(position=Vector2(1150, 1050)),
                     Rocket(position=Vector2(150, 250)),
                     Rocket(position=Vector2(250, 20)),
                     Rocket(position=Vector2(340, -40)),
                     Rocket(position=Vector2(190, 750)),
                     Rocket(position=Vector2(730, 160)),
                     Rocket(position=Vector2(340, 450)),
                     Rocket(position=Vector2(450, 700)),
                     Rocket(position=Vector2(690, 50)),
                     Rocket(position=Vector2(830, 360)),
                     Rocket(position=Vector2(400, 950)),
                     Rocket(position=Vector2(1000, 890)),
                     Rocket(position=Vector2(1060, 350)),
                     Rocket(position=Vector2(700, 800)),
                     Rocket(position=Vector2(290, 950)),
                     Rocket(position=Vector2(810, 260)),
                     Rocket(position=Vector2(940, 150)),
                     Rocket(position=Vector2(580, 790)),
                     Rocket(position=Vector2(530, 0)),
                     Rocket(position=Vector2(360, 50)),
                     Rocket(position=Vector2(970, 450)),
                     Rocket(position=Vector2(810, -40)),
                     Rocket(position=Vector2(440, 150)),
                     Rocket(position=Vector2(880, 90)),
                     Rocket(position=Vector2(940, -50)),
                     Rocket(position=Vector2(680, -20))
                     ])

default_pattern_8 = [
            Platform(physics=Physics(
                position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                width=SHAPE.x,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(2, BLOCK_HEIGHT * 2),
                width=4,
                height=PLAYER_SIZE.y + 16
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                width=2,
                height=PLAYER_SIZE.y + 16),
                color=arcade.color.CARIBBEAN_GREEN)
        ]


default_pattern_7 = [
            Platform(physics=Physics(
                position=Vector2(100, BLOCK_HEIGHT // 2),
                width=200,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 100, BLOCK_HEIGHT // 2),
                width=200,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(300, 200),
                width=50,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(900, 200),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                width=BLOCK_HEIGHT,
                height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(2, BLOCK_HEIGHT * 2),
                width=4,
                height=PLAYER_SIZE.y + 16
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                width=2,
                height=PLAYER_SIZE.y + 16),
                color=arcade.color.CARIBBEAN_GREEN
            ),
            Platform(physics=Physics(
                position=Vector2(125, 370),
                width=50,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(1050, 370),
                width=100,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(375, 465),
                width=50,
                height=BLOCK_HEIGHT
            )),
            Platform(physics=Physics(
                position=Vector2(SHAPE.x - 200 + BLOCK_HEIGHT // 2, 175),
                width=BLOCK_HEIGHT,
                height=350
            ))
        ]