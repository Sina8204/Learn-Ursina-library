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

########################### Input ###########################

# e = Entity(model= 'quad' , color = color.green)
# def input(key):
#     if key == "s":
#         e.y -= 1
#     elif key == "w":
#         e.y += 1
#     elif key == "a":
#         e.x -= 1
#     elif key == "d":
#         e.x += 1

# class Player(Entity):
#     def __init__(self):
#         super().__init__()
#         self.model = 'cube'
    
#     def input(self, key):
#         if key == 'w':
#             self.position += self.forward

#         if key == 'd':
#             self.animate('rotation_y', self.rotation_y + 90, duration=.5)

#         if key == 'a':
#             self.animate('rotation_y', self.rotation_y - 90, duration=.5)
# player = Player()
# # #player.model = 'cube'

########################### Input ###########################

########################### Mouse Input ###########################

# # mouse.hovered_entity
# # --> Returns the entity object that the mouse is currently over
# # --> Example: print(mouse.hovered_entity.name)
# # --> Returns None if mouse is not over any entity

# # Entity.hovered
# # --> Returns a boolean (True/False) indicating whether the mouse is over THIS entity
# # --> Example: if my_entity.hovered: print("Mouse is on me!")

# # Important: Both features require the entity to have a collider component
# # --> Add collider='box' to your entity: Entity(model='cube', collider='box')

# blue_cube = Entity(model = 'cube' , color = color.blue , position=Vec3(-2,0,0))
# green_cube = Entity(model = 'cube' , color = color.green , position=Vec3(0,0,0))
# red_cube = Entity(model = 'cube' , color = color.red , position=Vec3(2,0,0))

# blue_cube.collider = 'box'
# green_cube.collider = 'box'
# red_cube.collider = 'box'

# def input(key):
#     if key == "left mouse down" and blue_cube.hovered:
#         print(mouse.hovered_entity , "Blue cube")
#     elif key == "left mouse down" and green_cube.hovered:
#         print(mouse.hovered_entity , "Green cube")
#     elif key == "left mouse down" and red_cube.hovered:
#         print(mouse.hovered_entity , "Red cube")

########################### Mouse Input ###########################

########################### Some clicks functions ###########################

# # #on_click & double_click method
# #Entity(model='quad', parent=camera.ui, scale=.1, collider='box', on_click=action) # on_click should be a function/callable/Func/Sequence

# def action():
#     print('Ow! That hurt!')

# one_click_Entity = Entity(model='quad', position = Vec3(-2 , 0 , 0) , collider='box', on_click=action) # on_click should be a function/callable/Func/Sequence
# double_click_Entity = Entity(model='quad',  position = Vec3(0 , 0 , 0) , collider='box', on_double_click = lambda : print ("Ahhh , I died")) # double_click should be a function/callable/Func/Sequence

# #on_mouse_enter & on_mouse_exit methods
# b = Button(scale=(.5, .25), text='zzz')
# b.on_mouse_enter = Func(setattr, b, 'text', 'Hi, friend :D')
# b.on_mouse_exit = Func(setattr, b, 'text', '''No! Don't leave me ;-;''')


########################### Other Magic Functions  ###########################

# # on_enable() --> runs when entity.enabled = True (object activation)
# # Usage: restarting, starting animations, creating effects upon activation

# # on_disable() --> runs when entity.enabled = False (object deactivation)
# # Usage: stopping animations, saving state, cleaning up resources upon deactivation

# # on_destroy() --> runs right before destroy(entity) (complete object destruction)
# # Usage: playing final effects, freeing memory, recording stats upon destruction

# class MagicLamp(Entity):
#     def __init__(self, position=(0,0,0)):
#         super().__init__(
#             model='cube',
#             color=color.yellow,
#             scale=1,
#             collider='box',
#             position=position
#         )
#         self.is_lit = False
#         self.light_effect = None
        
#     def on_enable(self):
#         """When the lamp gets activated"""
#         print("🟢 Magic lamp activated!")
#         # Create a light effect around the lamp
#         self.light_effect = Entity(
#             model='sphere',
#             color=color.yellow,
#             scale=1.5,
#             position=self.position,
#             alpha=0.5
#         )
        
#     def on_disable(self):
#         """When the lamp gets deactivated"""
#         print("🔴 Magic lamp deactivated!")
#         # Remove the light effect
#         if self.light_effect:
#             destroy(self.light_effect)
#             self.light_effect = None
    
#     def on_destroy(self):
#         """Right before the lamp is destroyed"""
#         print("💥 Magic lamp destroyed!")
#         # Create a sparkling explosion
#         explosion = Entity(
#             model='sphere',
#             color=color.orange,
#             scale=0,
#             position=self.position
#         )
#         explosion.animate_scale(3, duration=0.5, curve=curve.out_elastic)
#         destroy(explosion, delay=0.5)
        
#         # Show a cool message
#         msg = Text(f"Lamp destroyed!", position=(0, 0.3), scale=2, color=color.red)
#         destroy(msg, delay=1)
    
#     def input(self, key):
#         if self.hovered:
#             if key == 'left mouse down':
#                 # Toggle on/off state
#                 self.is_lit = not self.is_lit
#                 if self.is_lit:
#                     self.color = color.gold
#                     print("✨ Lamp turned on!")
#                 else:
#                     self.color = color.yellow
#                     print("🌙 Lamp turned off!")
            
#             elif key == 'right mouse down':
#                 # Destroy the lamp with right click
#                 print("⚠️ Lamp is being destroyed...")
#                 destroy(self)  # This line triggers on_destroy()

# # Create lamp
# lamp = MagicLamp(position=(0, 0, 0))
# lamp.enabled = False  # Start deactivated

# # Button to activate/deactivate the lamp
# def toggle_lamp():
#     lamp.enabled = not lamp.enabled
#     status = "Activated" if lamp.enabled else "Deactivated"
#     print(f"💡 Lamp status: {status}")

# # Toggle button
# button = Button(
#     text='Activate/Deactivate Lamp',
#     color=color.azure,
#     scale=0.2,
#     position=(0, -0.4)
# )
# button.on_click = toggle_lamp

# # Instructions
# info = Text(
#     text="🖱️ Left Click: On/Off\n🖱️ Right Click: Destroy Lamp\n🔘 Bottom Button: Activate/Deactivate",
#     position=(-0.85, -0.4),
#     scale=1,
#     origin=(-0.5, 0)
# )

# EditorCamera()  # For camera movement

########################### Other Magic Functions  ###########################
app.run()
