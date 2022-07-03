import os
import random

from game.casting.item import Item
from game.casting.gemrock import Gemrock
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_GEMROCKS = 200


def main():
    
    # create the cast
    cast = Cast(COLS, ROWS, CELL_SIZE)

    # create the banner
    banner = Item()
    # banner.set_text("Score: ") #aquí le modifiqué score
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_item("banners", banner)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y - FONT_SIZE)

    position = Point(x, y)

    player = Item()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_item("players", player)
    

    characters = ["O", "*"]
    for n in range(DEFAULT_GEMROCKS):
        text = random.choice(characters)

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)

        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)        

        gemrock = Gemrock()
        gemrock.set_text(text)
        gemrock.set_font_size(FONT_SIZE)
        gemrock.set_color(color)
        gemrock.set_position(position)
        gemrock.set_velocity(Point(0,5))
        
        if text == "O":
            gemrock.set_points(-1)
        elif text == "*":
            gemrock.set_points(1)

        cast.add_item("gemrocks", gemrock)        
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()