from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Voxel(Button):
    def __init__(self, position=(0,0,0),color1 = color.rgb(255, 87, 51)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'grass',
            color = color1,
            highlight_color = color.lime,
           
            )

    def input(self,key):
        if self.hovered: 
            if key == "left mouse down":
                voxel = Voxel(position= self.position + mouse.normal,color1 = color.rgb(216,216,21))

            if key == "right mouse down": 
                destroy(self)    

chunkSize = 32

for z in range(chunkSize):
    for x in range(chunkSize):
        voxel = Voxel(position=(x,0,z))

player = FirstPersonController()    

app.run()