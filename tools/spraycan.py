from pygame import *
from random import *
width = 40

screen = display.set_mode((980, 750))
display.set_caption ("Paint")

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1 or evt.button == 3:
                omx, omy = evt.pos       #old mx, old my positions
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    if mb[0] == 1:
        xpos = randint(width * -1, width)
        ypos = randint(width * -1, width)
        if xpos ** 2 + ypos ** 2 <= width ** 2:
            draw.line(screen,(255,0,0),(mx + xpos, my + ypos),(mx + xpos, my + ypos),1)
    display.flip()
quit()
