from pygame import *

screen = display.set_mode((980, 750))
display.set_caption ("Paint")

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1 or evt.button == 3:
                omx, omy = evt.pos       #old mx, old my - used for drawing and dragging lines
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    if mb[0] == 1:
        draw.line(screen,(255,255,255),(omx,omy),(mx,my),50)
        omx,omy = mx,my
    
        

    display.flip()
quit()
