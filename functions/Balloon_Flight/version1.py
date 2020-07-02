import pgzrun
from random import randint
#set the screen
WIDTH=800
HEIGHT=600
# creating actor
balloon=Actor("balloon")
balloon.pos=400,300

bird=Actor("bird up")
house=Actor("")

pgzrun.go()