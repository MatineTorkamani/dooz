#pm
def display_message(content):
    pg.time.delay(700)
    SCREEN.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK)
    SCREEN.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pg.display.update()
    pg.time.delay(4000)
