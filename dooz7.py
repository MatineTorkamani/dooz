#mainloop
def main():
    global cat_turn, mouse_turn, images, draw

    images = []
    draw = False

    run = True

    cat_turn = True
    mouse_turn = False

    game_array = initial_grid()

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                click(game_array)

        render()

        if has_won(game_array) or has_drawn(game_array):
            run = False

while True:
    if __name__ == '__main__':
        main()
