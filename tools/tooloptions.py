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
green = (0,255,0)

screen = display.set_mode((126,201))
display.set_caption ("Paint")
background = image.load("images/tooloptions.png")

screen.blit(background,(0,0))

shapestyleRect1 = Rect(5,5,115,60) 
shapestyleRect2 = Rect(5,70,115,60)
shapestyleRect3 = Rect(5,135,115,60)

draw.rect(screen,green,shapestyleRect1,2)
draw.rect(screen,green,shapestyleRect2,2)
draw.rect(screen,green,shapestyleRect3,2)

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
       
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
   

    display.flip()
quit()
