import pygame as pg
import math

#intialization
pg.init()
disp= pg.display.set_mode((480,480))
WIDTH =480
HEIGHT=480
ROWS = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("dooze")
SCREEN.fill((WHITE))

#variables
done = False
cat_name='data/cat.png'
cat_img=pg.image.load(cat_name)
cat_img=pg.transform.scale(cat_img,(150,150))

mouse_name='data/mause.png'
mouse_img=pg.image.load(mouse_name)
maouse_img=pg.transform.scale(mouse_img,(150,150))

END_FONT = pg.font.SysFont('arial', 50)
