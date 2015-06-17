from pygame import *

screen = display.set_mode((980, 750))
display.set_caption ("Paint")
red = (255,0,0)
running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1 or evt.button == 3:
                omx, omy = evt.pos       #old mx, old my - used for drawing and dragging lines
                draw.circle(screen,red,(omx,omy),4)
                
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    if mb[0] == 1:
        draw.line(screen,red,(omx,omy),(mx,my),7)
        if mouse.get_rel() == (0,0):
            draw.circle(screen,red,(omx,omy),4)
        omx,omy = mx,my

    print mouse.get_rel()
        

    display.flip()
quit()

