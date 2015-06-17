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

screen = display.set_mode((200,201))
display.set_caption ("Paint")

saveRect = Rect(5,5,60,35)
loadRect = Rect(70,5,60,35)

draw.rect(screen,(255,0,0),saveRect,2)
draw.rect(screen,(255,0,0),loadRect,2)

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
       
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
   

    display.flip()
quit()
