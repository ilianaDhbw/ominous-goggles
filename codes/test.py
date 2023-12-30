import time
import turtle as t
from random import randint as rnd

colors = ["light blue","pink","purple","yellow"]
t.width (6) 

def tl(winkel,mass):
    t.color(colors[rnd(0,len(colors)-1)])
    t.left(winkel)
    t.forward(mass)
            
def tr(winkel,mass):
    t.color(colors[rnd(0,len(colors)-1)])
    t.right(winkel)
    t.forward(mass)
        
# Programm ablauf
tl(180,50)
tr(135,70)
tl(135,50)
tr(135,35)
tr(90,35)
tr(45,50)
tr(135,70)
tl(135,50)

t.done()