from ursina import *

app = Ursina()

########################### Models ###########################

#e1 = Entity(model='cube', texture='Asset/img.jpeg') # set a texture
#e4 = Entity(model='cube', texture='Asset/movie.mp4') # set video texture

########################### Models ###########################

########################### Texture ###########################

# s = Sprite('Asset/img.jpeg') 
# print(s.aspect_ratio)

########################### Texture ###########################

########################### Colors ###########################

# e = Sprite()
# e.color = color.red # set it to a color in the color module
# e.color = hsv(120, .5, .5) # hsv color
# e.color = rgb(.8, .1, 0) # rgb color
# e.color = '#aabbcc' # hex color
# e.color = e.color.tint(.1) # tint the color
# e.color = color.random_color() # set it to a random color
# e.color = lerp(color.red, color.green, .5) # set it to a color half way between red and green

########################### Colors ###########################

########################### Position ###########################

# e = Entity(model='cube') #Set relative position
# e.position = Vec3(0,0,0)
# e.position = Vec2(0,0)
# e.position = (0,0,0)
# e.position = (0,0)

# e2 = Entity(model='cube' , position=Vec3(1,1,1)) #Set Position by 'x' 'y' 'z'
# e2.x = 0
# print(e2.position)

# parent_entity = Entity(model = 'cube' , position=Vec3(0,2,0)) #Set position from an parent
# e = Entity(model = 'cube' , parent=parent_entity, position=Vec3(0,2,0))
# print(e.position)

# print(e.world_position)

# e.world_position = Vec3(0,0,0)
# print(e.position)

########################### Position ###########################

########################### Rotation ###########################

# e = Entity(model= 'cube')
# e.rotation = (0,0,0)
# e.rotation_y = 90

# other_entity = Entity(position=(10,1,8))
# e.look_at(other_entity) # make z-axis(forward) point at other_entity
# e.look_at(other_entity, axis='up') # optionally define which axis

########################### Rotation ###########################

########################### Scale ###########################

#e = Entity(model='cube', scale=(3,1,1))

########################### Scale ###########################

########################### Update ###########################

# e = Entity(model='cube')
# def my_update():
#     e.x += 1 * time.dt # dt is short for delta time, the duration since the last frame.

# e.update = my_update

# class Player(Entity):
#     def __init__(self):
#         super().__init__()
#         self.model = 'cube'
#         self.color = color.blue
#         self.speed = 2

#     def update(self):
#         self.x += self.speed * time.dt
#         if self.x > 5 or self.x < -5:
#             #self.x = -5
#             self.speed *= -1
    
# player = Player()

########################### Update ###########################

app.run()
