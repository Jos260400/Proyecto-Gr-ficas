#Universidad del Valle de Guatemala
#Graficas por Computadoras
#Fernando Jose Garavito Ovando 18071
#Proyecto
# Programa principal
from gl import Renderer, V3, _color
from obj import Texture
from shaders import *

import random

width = 960
height = 540

rend = Renderer(width, height)

rend.directional_light = V3(0,0,-1)

rend.active_texture = Texture('models/Color.bmp')
rend.normal_map = Texture('models/Color.bmp')

#Luna
rend.active_shader = normalMap
rend.glLoadModel("models/Moon.obj",
                 translate = V3(-3, 3, -10),
                 scale = V3(1,1,1))

#Planta
rend.active_shader = normalMapp
rend.glLoadModel("models/Plant.obj",
                 translate = V3(4, -5, -10),
                 scale = V3(1,1,1))

#Niña
rend.active_shader = phong
rend.glLoadModel("models/Girl.obj",
                 translate = V3(6, -5, -10),
                 scale = V3(1,1,1))

#Arbol
rend.active_shader = phongg
rend.glLoadModel("models/Tree.obj",
                 translate = V3(1, -5, -10),
                 scale = V3(1,1,1))

#Nave 
rend.active_shader = phonggg
rend.glLoadModel("models/Aircraft.obj",
                 translate = V3(5, 1, -10),
                 scale = V3(1,1,1))

rend.glFinish("Proyecto.bmp")


