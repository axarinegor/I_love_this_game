import arcade
import pyglet
from ..tools.physics import SHAPE

# Обычный пиксельный шрифт - Digital Upscaled Pixel
pyglet.font.add_file(r"yandex_arcade\data\Pixel_fonc.otf")
pixel_font = "Digital Upscaled Pixel"
BIG_SIZE = 30
MEDIUM_SIZE = 22
SMALL_SIZE = 16

NAME_LEVELS = {1:'1 - Знакомство',
               2:'2 - Прыжок веры',
               3:'3 - Секретные стены',
               4:'4 - Углы',
               5:'5 - Паспарту',
               6:'6 - Тыкай и рисуй!',
               7:'7 - Темнота',
               8:'8 - Ракеты!',
               9:'9 - Сапер',
               10:'10 - Колесо',
               11:'11 - Психотерапия',
               12:'12 - Имя, только имя',
               13:'13 - Циклоп',
               14:'14 - Прыгун',
               15:'15 - Странный алфавит',
               16:'16 - Альцгеймер',
               17:'17 - Гравитация',
               18:'18 - ЛКМ',
               19:'19 - Переключатель',
               20:'20 - Конец(',
               }
LEVEL_1 = [arcade.Text(
            text="Управление",
            x=380,
            y=500,
            color=arcade.color.BLACK,
            font_size=MEDIUM_SIZE,
            font_name=pixel_font,
            bold=True
           ), 
            arcade.Text(
            text="A/D - Вперёд/Назад",
            x=380,
            y=435,
            color=arcade.color.BLACK,
            font_size=SMALL_SIZE,
            font_name=pixel_font
           ), 
            arcade.Text(
            text="SPACE - Прыжок",
            x=380,
            y=370,
            color=arcade.color.BLACK,
            font_size=SMALL_SIZE,
            font_name=pixel_font
           ), 
            arcade.Text(
            text="ESC - Пауза",
            x=380,
            y=305,
            color=arcade.color.BLACK,
            font_size=SMALL_SIZE,
            font_name=pixel_font
           )]


LEVEL_2 = [arcade.Text(
            text="Прыжок веры",
            x=380,
            y=400,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]

LEVEL_3 = [arcade.Text(
            text="В стенах хранятся тайны",
            x=240,
            y=500,
            color=arcade.color.BLACK,
            font_size=MEDIUM_SIZE,
            font_name=pixel_font,
            bold=True
           )]


LEVEL_10 = [arcade.Text(
            text="Колёсико мыши",
            x=SHAPE.x // 2,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True,
            anchor_x="center",
            anchor_y="center"
           )]


LEVEL_13 = [arcade.Text(
            text="Циклоп",
            x=SHAPE.x // 2,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True,
            anchor_x="center",
            anchor_y="center"
           )]


LEVEL_5 = [arcade.Text(
            text="Ключик",
            x=810,
            y=300,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]



LEVEL_9 = [arcade.Text(
            text="Границы",
            x=SHAPE.x // 2,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True,
            anchor_x="center",
            anchor_y="center"
           )]


LEVEL_6 = [arcade.Text(
            text="Тыкай, рисуй!",
            x=460,
            y=530,
            color=arcade.color.BLACK,
            font_size=MEDIUM_SIZE,
            font_name=pixel_font,
            bold=True
           )]


LEVEL_14 = [arcade.Text(
            text="Только",
            x=480,
            y=530,
            color=arcade.color.BLACK,
            font_size=MEDIUM_SIZE,
            font_name=pixel_font,
            bold=True
           ),
           arcade.Text(
            text="в прыжке",
            x=480,
            y=470,
            color=arcade.color.BLACK,
            font_size=MEDIUM_SIZE,
            font_name=pixel_font,
            bold=True
           )]

LEVEL_20 = [arcade.Text(
            text="Спасибо большое за прохождение!",
            x=150,
            y=510,
            color=arcade.color.BLACK,
            font_size=MEDIUM_SIZE,
            font_name=pixel_font,
            bold=True
           ),
           arcade.Text(
            text="игра, а сам проект темболее)",
            x=280,
            y=320,
            color=arcade.color.BLACK,
            font_size=SMALL_SIZE,
            font_name=pixel_font,
            bold=True
           ),
           arcade.Text(
            text="Я надеюсь, вам понравилась",
            x=280,
            y=380,
            color=arcade.color.BLACK,
            font_size=SMALL_SIZE,
            font_name=pixel_font,
            bold=True
           ),
           ]

LEVEL_17 = [arcade.Text(
            text='<><><><><>',
            x=500,
            y=350,
            color=arcade.color.BLACK,
            font_size=MEDIUM_SIZE,
            font_name=pixel_font,
            bold=True
           )]

LEVEL_19 = [arcade.Text(
            text='Переключатель',
            x=650,
            y=420,
            color=arcade.color.BLACK,
            font_size=MEDIUM_SIZE,
            font_name=pixel_font,
            bold=True
           )]

LEVEL_4 = [arcade.Text(
            text="Углы",
            x=250,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]


LEVEL_18 = [arcade.Text(
            text="ЛКМ",
            x=530,
            y=400,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]


LEVEL_12 = [arcade.Text(
            text="Как зовут создателя?",
            x=200,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]


LEVEL_15 = [arcade.Text(
            text=".....",
            x=380,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           ),
           arcade.Text(
            text="...--",
            x=535,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           ),
           arcade.Text(
            text="----.",
            x=710,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           ),
           ]


LEVEL_7 = [arcade.Text(
            text="Темнота",
            x=400,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]

LEVEL_8 = [arcade.Text(
            text="Ракеты!",
            x=460,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]