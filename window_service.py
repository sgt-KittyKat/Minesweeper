import sweeperlib


def create_window(height, width, handler):
    sweeperlib.load_sprites("/Minesweeper/resources/sprites")
    sweeperlib.create_window(width, height)
    sweeperlib.set_draw_handler(handler)
    sweeperlib.start()

