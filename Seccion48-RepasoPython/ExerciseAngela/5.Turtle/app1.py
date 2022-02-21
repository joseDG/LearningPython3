#Importaciones
#from turtle import Turtle
#from turtle import * permite importar todo los paquetes de ese modulo
#import turtle as t => se llaman alias 

import turtle as t 
import random

tim = t.Turtle()

colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)