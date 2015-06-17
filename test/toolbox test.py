#Paint.py
#Nikola Zjalic

#TO DO
##move pallette over to make tool bar bigger
##make a theme
##background
##find a place for the pallette icon
##save image
##undo, redo
##stamp menu
##allow user to import stamp?
##show the current width of line


from pygame import *

screen = display.set_mode((127,387))
display.set_caption ("Paint")
background = image.load("images/toolbox.png")

eyedropperhover = image.load("images/eyedropperhover.png")
eraserhover = image.load("images/eraserhover.png")
pencilhover = image.load("images/pencilhover.png")
linehover = image.load("images/linehover.png")
paintbrushhover = image.load("images/paintbrushhover.png")
paintcanhover = image.load("images/paintcanhover.png")
spraycanhover = image.load("images/spraycanhover.png")
stampshover = image.load("images/stampshover.png")
boxhover = image.load("images/boxhover.png")
ellipsehover = image.load("images/ellipsehover.png")
undohover = image.load("images/undohover.png")
redohover = image.load("images/redohover.png")

eyedropperRect = Rect(0,0,60,60)
eraserRect = Rect(65,0,60,60)
pencilRect = Rect(0,65,60,60)
lineRect = Rect(65,65,60,60)
paintbrushRect = Rect(0,130,60,60)
paintcanRect = Rect(65,130,60,60)
spraycanRect = Rect(0,195,60,60)
stampsRect = Rect(65,195,60,60)
boxRect = Rect(0,260,60,60)
ellipseRect = Rect(65,260,60,60)
undoRect = Rect(0,325,60,60)
redoRect = Rect(65,325,60,60)



running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
       
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()

    screen.blit(background,(0,0))

    if eyedropperRect.collidepoint(mx,my):
        screen.blit(eyedropperhover,(0,0))
    if eraserRect.collidepoint(mx,my):
        screen.blit(eraserhover,(65,0))
    if pencilRect.collidepoint(mx,my):
        screen.blit(pencilhover,(0,65))
    if lineRect.collidepoint(mx,my):
        screen.blit(linehover,(65,65))
    if paintbrushRect.collidepoint(mx,my):
        screen.blit(paintbrushhover,(0,130))
    if paintcanRect.collidepoint(mx,my):
        screen.blit(paintcanhover,(65,130))
    if spraycanRect.collidepoint(mx,my):
        screen.blit(spraycanhover,(0,195))
    if stampsRect.collidepoint(mx,my):
        screen.blit(stampshover,(65,195))
    if boxRect.collidepoint(mx,my):
        screen.blit(boxhover,(0,260))
    if ellipseRect.collidepoint(mx,my):
        screen.blit(ellipsehover,(65,260))
    if undoRect.collidepoint(mx,my):
        screen.blit(undohover,(0,325))
    if redoRect.collidepoint(mx,my):
        screen.blit(redohover,(65,325))

    

    display.flip()
quit()
