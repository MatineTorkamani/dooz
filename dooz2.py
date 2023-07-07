
#jadval
def draw_grid():
    gap = WIDTH // ROWS

    x = 0
    y = 0

    for i in range(ROWS):
        x = i * gap
        pygame.draw.line(window, BLACK, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(window, BLACK, (0, x), (WIDTH, x), 3)

def initial_grid():
    dis_to_center = WIDTH // ROWS // 2

    game_array = [[None, None, None], [None, None, None], [None, None, None]]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_center * (2 * j + 1)
            y = dis_to_center * (2 * i + 1)

            game_array[i][j] = (x, y,"", True)

    return game_array


def click(game_array):
    global cat_turn, mouse_turn, images

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char, can_play = game_array[i][j]

            dis = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)

            if dis < WIDTH // ROWS // 2 and can_play:
                if cat_turn:  
                    images.append((x, y, CAT_IMAGE))
                    cat_turn = False
                    mouse_turn = True
                    game_array[i][j] = (x, y, 'cat', False)

                elif mouse_turn:  
                    images.append((x, y, MOUSE_IMAGE))
                    cat_turn = True
                    mouse_turn = False
                    game_array[i][j] = (x, y, 'mouse', False)

#barande
def has_won(game_array):
    for row in range(len(game_array)):
        if (game_array[row][0][2] == game_array[row][1][2] == game_array[row][2][2]) and game_array[row][0][2] != "":
            display_message(game_array[row][0][2].upper() + " You Won! ")
            return True

    for col in range(len(game_array)):
        if (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2]) and game_array[0][col][2] != "":
            display_message(game_array[0][col][2].upper() + " You Won! ")
            return True

    if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
        display_message(game_array[0][0][2].upper() + " You Won! ")
        return True

    if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
        display_message(game_array[0][2][2].upper() + " You Won! ")
        return True

    return False
