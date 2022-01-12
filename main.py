from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('assets/grass.png')
dirt_texture = load_texture('assets/dirt.png')
oak_texture = load_texture('assets/oak.png')
sand_texture = load_texture('assets/sand.png')
stone_texture = load_texture('assets/stone.png')
wood_texture = load_texture('assets/wood.png')
leaf_texture = load_texture('assets/leaf.png')
brick_texture = load_texture('assets/brick.png')
birch_texture = load_texture('assets/birch.png')
glass_texture = load_texture('assets/glass.png')
iron_texture = load_texture('assets/iron.png')
diamond_texture = load_texture('assets/diamond.png')
gold_texture = load_texture('assets/gold.png')
emerald_texture = load_texture('assets/emerald.png')
sky_texture = load_texture('assets/sky.png')

current_texture = grass_texture

def update():
    global current_texture

    if held_keys['1']:
        current_texture = grass_texture

    if held_keys['2']:
        current_texture = dirt_texture

    if held_keys['3']:
        current_texture = oak_texture

    if held_keys['4']:
        current_texture = sand_texture

    if held_keys['5']:
        current_texture = stone_texture

    if held_keys['6']:
        current_texture = wood_texture

    if held_keys['7']:
        current_texture = leaf_texture

    if held_keys['8']:
        current_texture = birch_texture

    if held_keys['9']:
        current_texture = brick_texture

    if held_keys['0']:
        current_texture = glass_texture

    if held_keys['/']:
        current_texture = iron_texture

    if held_keys['*']:
        current_texture = diamond_texture

    if held_keys['-']:
        current_texture = gold_texture

    if held_keys['+']:
        current_texture = emerald_texture
  
class sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            scale = 150,
            texture = sky_texture,
            double_sided = True
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            scale = (0.2, 0.3),
            color = color.white,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.4)
        ) 


    def active(self):
        self.position = Vec2(0.1, -0.5)
        self.rotation = Vec3(90, -10, 0)

    def passive(self):
        self.rotation = Vec3(150, -10, 0)
        self.position = Vec2(0.4, -0.4)   
    
class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = texture,
            color = color.color(0, 0, 255),
            highilight_color = color.lime
            )
    

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position = self.position + mouse.normal, texture = current_texture)
            if key == 'right mouse down':
                destroy(self)


for x in range(20):
    for z in range(20):
        voxel = Voxel(position = (x,0,z))

#for z in range(8):
#    for x in range(8):
#        for y in range(8):
#            voxel - Voxel((x, z, y))


player = FirstPersonController()
sky = sky()
hand = Hand()
app.run()