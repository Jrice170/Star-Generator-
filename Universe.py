# Joseph Rice 12/27/2017
from visual import *
from math import sqrt as root
from random import *
import datetime
now = datetime.datetime.today()
print("The current date is:",now)

scene.width = 1000
scene.height = 1000
scene.title = 'Star Generator'
### Add a shoting star.
print('Makes a cool desktop background !')
print("__This serves as a simulation of stars being born in a universe of 0's and 1's__")


class universe():
    # keep this as a defult for the other universes
    # radius; starting radius, posx;poxy;posz position of circle
    def __init__(self,radius,posx,posy,posz,color,opacity):
        self.radius,self.expanstion,self.posx,self.posy,self.posz,self.color,\
        self.opacity = radius,0.01,posx,posy,posz,color,opacity
        self.ball = sphere(pos=vector(self.posx,self.posy,self.posz),\
        radius=self.radius,color=self.color,opacity=self.opacity)
    def replicate(self,expanstion):
        self.expanstion += expanstion
        list_value,color_list = [10000,40000,10009,int(20500),\
        int(10000*random())/4,\
        int(2000*random()),int(root(29999*random()))/2,11379,int(random()\
        *119700/1.5),21700,\
        5814,97070*random(),int(55110*random()),85287*random()],\
        [color.cyan,color.yellow,color.red,color.blue,\
        color.magenta,color.green,color.magenta,color.white]
        value,value2 = randrange(0,14),randrange(0,7)
        x,y,z=randrange(-10000*20,10000*20),randrange(-10000*20,10000*20),\
        randrange(-10000*20,10000*20)
        unv = sphere(pos=vector(x,y,z),radius=self.radius,color=color_list[value2],\
        opacity=self.opacity,material=materials.emissive)
        for i in range(0,int(list_value[value])):
            unv.radius += self.expanstion
number_of_universes,n = eval(input("Enter number of universes: ")),0
print("Bang!!!!!!!!!!!")
while n <= int(number_of_universes):
    n+=1
    def_v = universe(0,0,0,0,color.white,0.5)
    def_v.replicate(0.01)
list = []
count = 0
process = 'Happy programing!'
for i in process:

    list.append(ord(i))
str_str = ''
for i in list:
    str_str +=  str(bin(i)) + " "
print(str_str)
