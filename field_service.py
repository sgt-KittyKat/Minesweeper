import random
from game_data import *
import field
import sweeperlib
import tile


def generate_field(data):
    playfield = field.Field()
    for row in range(data["number of rows"]):
        current_row = []
        for column in range(data["number of columns"]):
            current_row.append(tile.Tile(" ", False))
        playfield.field.append(current_row)
    return field


def explore_tile(char):
    if char == "x":
        return 1
    return 0


def is_in_field(col, row, playfield):
    if col in range(0, len(playfield[0])) \
            and row in range(0, len(playfield)):
        return True
    return False


def count_mines(col, row, playfield):
    counter = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            next_tile = [col + j, row + i]
            if is_in_field(next_tile[0], next_tile[1], playfield):
                counter += explore_tile(playfield[row + i][col + j].content)
    return counter


def draw_field(playfield):
    sweeperlib.clear_window()
    sweeperlib.draw_background()
    sweeperlib.begin_sprite_draw()
    for i in range(len(playfield)):
        for j in range(len(playfield[i])):
            sweeperlib.prepare_sprite(playfield[i][j], SPRITE_WIDTH * j, SPRITE_HEIGHT * i)
    sweeperlib.draw_sprites()


def explore_field(playfield):
    for i in range(len(playfield)):
        for j in range(len(playfield[i])):
            count_mines(j, i, playfield)


def place_mines(data, playfield):
    mines = data["number of mines"]
    mined_tiles = []
    while mines:
        row = random.randint(0, data["number of rows"] - 1)
        column = random.randint(0, data["number of columns"] - 1)
        if [row, column] not in mined_tiles:
            mined_tiles.append([row, column])
            mines -= 1
    for cur_tile in mined_tiles:
        playfield[cur_tile[0]][cur_tile[1]].content = "x"
