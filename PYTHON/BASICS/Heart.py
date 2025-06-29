import math
from turtle import *
def hearta(k):
    return 15*math.sin(k)**23
               
def heartb(k):
    return 12*math.cos(k)-5*\
        math.cos( 2*k)-2*\
            math.cos(3*k)-\
                math.cos(4*k)
    
    speed(0)
    bgcolor("black")
    for k in range(1000):
        goto(hearta())