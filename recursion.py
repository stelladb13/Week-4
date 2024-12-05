""" #Stella Bertoli 12/5/24
from random import * #importing random module

def randomNumber(times): #function named randomNumber and parameter of times
    if(times==0):  
        print('Stop!')
    else:
        print(randint(0,100))
   #     randomNumber(times-1) #Call Function itself
#randomNumber(5)  """

import turtle
tommy = turtle.Turtle()
def koch (sideLength, level):
    if level>0:
        for angle in [60,-120,60,0]:
            koch(sideLength/3,level-1)
            tommy.left(angle)
    else: 
        tommy.forward(sideLength)

koch(100,3)
turtle.done()
    
