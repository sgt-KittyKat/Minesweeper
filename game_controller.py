import field_service
import window_service


def init_game(game_data, field_data):
    window_service.create_window(game_data.WINDOW_HEIGHT, game_data.WINDOW_WIDTH)
    playfield = field_service.generate_field(field_data)
    field_service.draw_field(playfield)
    #todo finish this shit

def end_game(win):
    if not win:
        defeat()
    else:
        victory()
    record_results()


def record_results():


def update():


def process_tile(tile):


def add_tiles(col, row, playfield, tiles):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if field_service.is_in_field(col + i, row + j, playfield) \
                    and playfield[row + i][col + j] == ' ' and not tiles.count([col + j, row + i]):
                tiles.append([col + j, row + i])
    return tiles


def floodfill(playfield, x1, y1):
    tiles = [[x1, y1]]
    if playfield[y1][x1] == 'x':
        return
    while len(tiles):
        tile = tiles[0]
        tiles.remove(tiles[0])
        x = tile[0]
        y = tile[1]
        playfield[y][x].status = True
        tiles = add_tiles(x, y, playfield, tiles)

def victory():
    print("You still suck")

def defeat():
    print("You suck")