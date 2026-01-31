from dataclasses import dataclass
from pathlib import Path
import arcade
from ..game_items.block import Platform
from ..game_items.digit_block import DIGIT_BLOCK_WIDTH, DigitBlock
from ..draw import PLAYER_SIZE
from ..game_items.rocket import Rocket, Rockets
from ..tools.vector import Vector2
from ..tools.physics import Physics, SHAPE, BLOCK_HEIGHT

default_pattern_1 = [
            Platform(_physics=Physics(
                _position=Vector2(200, BLOCK_HEIGHT // 2),
                _width=400,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 200, BLOCK_HEIGHT // 2),
                _width=400,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(500, 200),
                _width=100,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(700, 200),
                _width=100,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
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
            8: default_pattern_8,
            16: default_pattern_16,
            17: default_pattern_17,
            19: default_pattern_19,
            15: default_pattern_15,
            14: default_pattern_14,
            5: default_pattern_5,
            18: default_pattern_18,
            9: default_pattern_9,
            13: default_pattern_13,
            10: default_pattern_10
        }
        
        return patterns.get(x, default_pattern_1)
    
    def get_default_block() -> arcade.Texture:
        texture_path = Path("yandex_arcade/data/block.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_default_door() -> arcade.Texture:
        texture_path = Path("yandex_arcade/data/door.jpg")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_default_rocket() -> arcade.Texture:
        texture_path = Path("yandex_arcade/data/rocket.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_intro_picture() -> arcade.Texture:
        texture_path = Path("yandex_arcade/data/intro.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_level_picture() -> arcade.Texture:
        texture_path = Path("yandex_arcade/data/level_select.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_key_texture() -> arcade.Texture:
        texture_path = Path("yandex_arcade/data/keyy.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_default_chain() -> arcade.Texture:
        texture_path = Path("yandex_arcade/data/chain.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_default_sofa() -> arcade.Texture:
        texture_path = Path("yandex_arcade/data/sofa.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)

    def get_default_lampa() -> arcade.Texture:
        texture_path = Path("yandex_arcade/data/lampa.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)
    
    def get_default_cat() -> arcade.Texture:
        texture_path = Path("yandex_arcade/data/cat.png")
        assert texture_path.exists()
        return arcade.load_texture(texture_path)

default_pattern_2 = [
            Platform(_physics=Physics(
                _position=Vector2(200, BLOCK_HEIGHT // 2),
                _width=400,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 200, BLOCK_HEIGHT // 2),
                _width=400,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(800, -100),
                _width=500,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]

default_pattern_3 = [
            Platform(_physics=Physics(
                _position=Vector2(200, BLOCK_HEIGHT // 2),
                _width=400,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(-2, SHAPE.y // 2),
                _width=4,
                _height=SHAPE.y
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 200, BLOCK_HEIGHT // 2),
                _width=400,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT * 3 + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT * 5
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT * 1.5),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(550, 370),
                _width=600,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]

default_pattern_4 = [
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            ),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 - 25, 300),
                _width=450,
                _height=BLOCK_HEIGHT)
            ),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 - 340, 150),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT)
            ),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 + 340, 150),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT)
            ),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 - 225, 150),
                _width=BLOCK_HEIGHT,
                _height=300)
            ),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 + 175, 150),
                _width=BLOCK_HEIGHT,
                _height=300)
            )
        ]


default_pattern_17 = [
            Platform(_physics=Physics(
                _position=Vector2(2 * BLOCK_HEIGHT, BLOCK_HEIGHT // 2),
                _width=BLOCK_HEIGHT * 4,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 2 * BLOCK_HEIGHT, BLOCK_HEIGHT // 2),
                _width=BLOCK_HEIGHT * 4,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 12, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=BLOCK_HEIGHT * 4,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(11 * SHAPE.x // 12, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=BLOCK_HEIGHT * 4,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]


default_pattern_6 = [
            Platform(_physics=Physics(
                _position=Vector2(300, BLOCK_HEIGHT // 2),
                _width=600,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(225, 250),
                _width=BLOCK_HEIGHT,
                _height=500
            )),
            Platform(_physics=Physics(
                _position=Vector2(425, SHAPE.y - 250),
                _width=BLOCK_HEIGHT,
                _height=500
            )),
            Platform(_physics=Physics(
                _position=Vector2(625, 250),
                _width=BLOCK_HEIGHT,
                _height=500
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 3.5 * BLOCK_HEIGHT, 250),
                _width=BLOCK_HEIGHT,
                _height=500
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 7.5 * BLOCK_HEIGHT, SHAPE.y - 200),
                _width=BLOCK_HEIGHT,
                _height=400
            )),
            Platform(_physics=Physics(
                _position=Vector2(300, 475),
                _width=2 * BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(350, 335),
                _width=2 * BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(475, 475),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(575, 475),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(300, 175),
                _width=2 * BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]


default_pattern_14 = [
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(225, 250),
                _width=BLOCK_HEIGHT,
                _height=500
            )),
            Platform(_physics=Physics(
                _position=Vector2(425, SHAPE.y - 250),
                _width=BLOCK_HEIGHT,
                _height=500
            )),
            Platform(_physics=Physics(
                _position=Vector2(775, 220),
                _width=BLOCK_HEIGHT,
                _height=450
            )),
            Platform(_physics=Physics(
                _position=Vector2(725, BLOCK_HEIGHT * 5.5),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(525, BLOCK_HEIGHT * 1.5),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(575, BLOCK_HEIGHT * 2.5),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(625, BLOCK_HEIGHT * 3.5),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(675, BLOCK_HEIGHT * 4.5),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 4.5 * BLOCK_HEIGHT, BLOCK_HEIGHT * 4.5),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 6.5 * BLOCK_HEIGHT, BLOCK_HEIGHT * 8.5),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 3.5 * BLOCK_HEIGHT, 250),
                _width=BLOCK_HEIGHT,
                _height=500
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 7.5 * BLOCK_HEIGHT, SHAPE.y - 200),
                _width=BLOCK_HEIGHT,
                _height=400
            )),
            Platform(_physics=Physics(
                _position=Vector2(300, 475),
                _width=2 * BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(350, 335),
                _width=2 * BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(175, 150),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(75, 350),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(300, 175),
                _width=2 * BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]


default_pattern_10 = [
            Platform(_physics=Physics(
                _position=Vector2(100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]


default_pattern_12 = [
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN)
        ]

Rockets_8 = Rockets([Rocket(_position=Vector2(150, 1050)),
                     Rocket(_position=Vector2(1150, 1050)),
                     Rocket(_position=Vector2(150, 250)),
                     Rocket(_position=Vector2(250, 20)),
                     Rocket(_position=Vector2(340, -40)),
                     Rocket(_position=Vector2(190, 750)),
                     Rocket(_position=Vector2(730, 160)),
                     Rocket(_position=Vector2(340, 450)),
                     Rocket(_position=Vector2(450, 700)),
                     Rocket(_position=Vector2(690, 50)),
                     Rocket(_position=Vector2(830, 360)),
                     Rocket(_position=Vector2(400, 950)),
                     Rocket(_position=Vector2(1000, 890)),
                     Rocket(_position=Vector2(1060, 350)),
                     Rocket(_position=Vector2(700, 800)),
                     Rocket(_position=Vector2(290, 950)),
                     Rocket(_position=Vector2(810, 260)),
                     Rocket(_position=Vector2(940, 150)),
                     Rocket(_position=Vector2(580, 790)),
                     Rocket(_position=Vector2(530, 0)),
                     Rocket(_position=Vector2(360, 50)),
                     Rocket(_position=Vector2(970, 450)),
                     Rocket(_position=Vector2(810, -40)),
                     Rocket(_position=Vector2(440, 150)),
                     Rocket(_position=Vector2(880, 90)),
                     Rocket(_position=Vector2(940, -50)),
                     Rocket(_position=Vector2(680, -20))
                     ])

default_pattern_8 = [
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN)
        ]


default_pattern_7 = [
            Platform(_physics=Physics(
                _position=Vector2(100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(300, 200),
                _width=50,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(900, 200),
                _width=100,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            ),
            Platform(_physics=Physics(
                _position=Vector2(125, 370),
                _width=50,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(1050, 370),
                _width=100,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(375, 465),
                _width=50,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 200 + BLOCK_HEIGHT // 2, 175),
                _width=BLOCK_HEIGHT,
                _height=350
            ))
        ]


default_pattern_16 = [
            Platform(_physics=Physics(
                _position=Vector2(100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            ),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            ))
        ]



default_pattern_15 = [
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]


default_pattern_5 = [
            Platform(_physics=Physics(
                _position=Vector2(75, BLOCK_HEIGHT // 2),
                _width=150,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 - 100, SHAPE.y - 3.5 * BLOCK_HEIGHT),
                _width=SHAPE.x - 200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 50, BLOCK_HEIGHT // 2),
                _width=100,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(250, 200),
                _width=100,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(500, 100),
                _width=100,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(500, 300),
                _width=100,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(700, 300),
                _width=100,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(900, 200),
                _width=100,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 75, SHAPE.y - 7.5 * BLOCK_HEIGHT),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]
y_9 = 340
digit_blocks_9 = [DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2, y_9),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2 + DIGIT_BLOCK_WIDTH, y_9),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2 - DIGIT_BLOCK_WIDTH, y_9),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2, y_9 - DIGIT_BLOCK_WIDTH),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2 + DIGIT_BLOCK_WIDTH, y_9 - DIGIT_BLOCK_WIDTH),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2 + 2 * DIGIT_BLOCK_WIDTH, y_9 - DIGIT_BLOCK_WIDTH),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2 - DIGIT_BLOCK_WIDTH, y_9 - DIGIT_BLOCK_WIDTH),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2 - 2 * DIGIT_BLOCK_WIDTH, y_9 - DIGIT_BLOCK_WIDTH),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2, y_9 - 2 * DIGIT_BLOCK_WIDTH),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2 + DIGIT_BLOCK_WIDTH, y_9 - 2 * DIGIT_BLOCK_WIDTH),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2 - DIGIT_BLOCK_WIDTH, y_9 - 2 * DIGIT_BLOCK_WIDTH),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    )),
                    DigitBlock(
                    _physics=Physics(
                    _position=Vector2(SHAPE.x // 2, y_9 - 3 * DIGIT_BLOCK_WIDTH - 15),
                    _width=DIGIT_BLOCK_WIDTH,
                    _height=DIGIT_BLOCK_WIDTH,
                    _is_active=False
                    ))
                    ]


default_pattern_9 = [
            Platform(_physics=Physics(
                _position=Vector2(200, BLOCK_HEIGHT // 2),
                _width=400,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 200, BLOCK_HEIGHT // 2),
                _width=400,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 - 200, 200),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 + 200, 200),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]


default_pattern_13 = [
            Platform(_physics=Physics(
                _position=Vector2(100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 - 150, 200),
                _width=BLOCK_HEIGHT, 
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(75, 225),
                _width=BLOCK_HEIGHT, 
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 + 300, 200),
                _width=BLOCK_HEIGHT * 2,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2 + 25, 300),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]



default_pattern_18 = [
            Platform(_physics=Physics(
                _position=Vector2(200, BLOCK_HEIGHT // 2),
                _width=400,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 200, BLOCK_HEIGHT // 2),
                _width=400,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT * 4),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT * 6
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, SHAPE.y - 70),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT * 3
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1.5 * BLOCK_HEIGHT, BLOCK_HEIGHT * 4.5),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, SHAPE.y // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(-2, SHAPE.y // 2),
                _width=4,
                _height=SHAPE.y
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x + 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]



default_pattern_19 = [
            Platform(_physics=Physics(
                _position=Vector2(100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(75, SHAPE.y - 3 * BLOCK_HEIGHT - 25),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(850, SHAPE.y - 1.5 * BLOCK_HEIGHT),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 75, 250),
                _width=BLOCK_HEIGHT,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 100, BLOCK_HEIGHT // 2),
                _width=200,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 10 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 10 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - BLOCK_HEIGHT // 2, PLAYER_SIZE.y + 15 + BLOCK_HEIGHT + (SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT) // 2),
                _width=BLOCK_HEIGHT,
                _height=SHAPE.y - PLAYER_SIZE.y - 15 - BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x // 2, SHAPE.y - BLOCK_HEIGHT // 2),
                _width=SHAPE.x,
                _height=BLOCK_HEIGHT
            )),
            Platform(_physics=Physics(
                _position=Vector2(2, BLOCK_HEIGHT * 2),
                _width=4,
                _height=PLAYER_SIZE.y + 16
            )),
            Platform(_physics=Physics(
                _position=Vector2(SHAPE.x - 1, BLOCK_HEIGHT + PLAYER_SIZE.y // 2 + 8),
                _width=2,
                _height=PLAYER_SIZE.y + 16),
                _color=arcade.color.CARIBBEAN_GREEN
            )
        ]


blocks_19_1 = [Platform(_physics=Physics(
               _position=Vector2(300, 150), 
               _width=BLOCK_HEIGHT, 
               _height=BLOCK_HEIGHT)),
            Platform(_physics=Physics(
               _position=Vector2(400, 450), 
               _width=BLOCK_HEIGHT, 
               _height=BLOCK_HEIGHT)),
            Platform(_physics=Physics(
               _position=Vector2(700, 270), 
               _width=BLOCK_HEIGHT, 
               _height=BLOCK_HEIGHT))
]

blocks_19_2 = [Platform(_physics=Physics(
               _position=Vector2(200, 350), 
               _width=BLOCK_HEIGHT, 
               _height=BLOCK_HEIGHT)),
            Platform(_physics=Physics(
               _position=Vector2(500, 450), 
               _width=BLOCK_HEIGHT, 
               _height=BLOCK_HEIGHT)),
            Platform(_physics=Physics(
               _position=Vector2(900, 290), 
               _width=BLOCK_HEIGHT, 
               _height=BLOCK_HEIGHT))
]