#update
def render():
    SCREEN.fill(WHITE)
    draw_grid()

    for image in images:
        x, y, IMAGE = image
        SCREEN.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pg.display.update()
