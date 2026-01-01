import arcade
import pyglet

# Обычный пиксельный шрифт - Digital Upscaled Pixel
pyglet.font.add_file("data/Pixel_fonc.otf")
pixel_font = "Digital Upscaled Pixel"
BIG_SIZE = 30
MEDIUM_SIZE = 22
SMALL_SIZE = 16

NAME_LEVELS = {1:'1 - Знакомство',
               2:'2 - Прыжок веры',
               3:'3 - Секретные стены',
               4:'4 - Углы',
               5:'5 - ',
               6:'6 - ',
               7:'7 - Темнота',
               8:'8 - Ракеты!',
               9:'9 - ',
               10:'10 - ',
               11:'11 - ',
               12:'12 - Имя, только имя',
               13:'13 - ',
               14:'14 - ',
               15:'15 - ',
               16:'16 - ',
               17:'17 - ',
               18:'18 - ',
               19:'19 - ',
               20:'20 - ',
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
            text="P - Пауза",
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


LEVEL_4 = [arcade.Text(
            text="Углы",
            x=250,
            y=500,
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