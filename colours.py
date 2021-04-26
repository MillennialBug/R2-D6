from discord import Colour
from random import seed, randint
from datetime import datetime

seed(datetime.now())
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

colours = [Colour.teal(), Colour.dark_teal(), 
           Colour.green(), Colour.dark_green(),
           Colour.blue(), Colour.dark_blue(),
           Colour.purple(), Colour.dark_purple(),
           Colour.magenta(), Colour.dark_magenta(),
           Colour.gold(), Colour.dark_gold(),
           Colour.orange(), Colour.dark_orange(),
           Colour.red(), Colour.dark_red(), 
           Colour.lighter_grey(), Colour.light_grey(),
           Colour.dark_grey(), Colour.darker_grey(),
           Colour.blurple(), Colour.greyple(),
           Colour.from_rgb(r, g, b)]
