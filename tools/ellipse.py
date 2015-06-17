from pygame import *
from random import *
width = 10

screen = display.set_mode((980, 750))
display.set_caption ("Paint")

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1 or evt.button == 3:
                back = screen.copy()
                omx, omy = evt.pos       #old mx, old my positions
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    
##    if mb[0] == 1:
##        x_small = min(omx,mx)
##        x_big = max(omx,mx)
##        y_small = min(omy,my)
##        y_big = max(omy,my)
##        screen.blit(back,(0,0))
##        draw.ellipse(screen,(255,0,0),(x_small,y_small,(x_big - x_small),(y_big - y_small)))
    if mb[0] == 1:
            x_small = min(omx,mx)
            x_big = max(omx,mx)
            y_small = min(omy,my)
            y_big = max(omy,my)
            if (x_big - x_small) / 2 > width and (y_big - y_small) / 2 > width:
                screen.blit(back,(0,0))
                draw.ellipse(screen,(255,0,0),(x_small,y_small,(x_big - x_small),(y_big - y_small)),width)
    if mb[2] == 1:
        x_small = min(omx,mx)
        x_big = max(omx,mx)
        y_small = min(omy,my)
        y_big = max(omy,my)
        if (x_big - x_small) / 2 > width and (y_big - y_small) / 2 > width:
            screen.blit(back,(0,0))
            draw.ellipse(screen,(0,255,0),(x_small,y_small,(x_big - x_small),(y_big - y_small)))
            draw.ellipse(screen,(255,0,0),(x_small,y_small,(x_big - x_small),(y_big - y_small)),width)
        
    display.flip()
quit()
