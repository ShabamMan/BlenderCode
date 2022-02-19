import bpy
from math import radians
import math
from random import seed
from random import random

seed(3)

def rect(r, theta):
    """theta in degrees

    returns tuple; (float, float); (x,y)
    """
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return x,y

for j in range(5):
    seed(j)
    for i in range(12):
    
        if i < 60:
        
            bpy.ops.mesh.primitive_uv_sphere_add()
            so = bpy.context.active_object
            
            
            xy = rect(5,i * 30 + (j*10))
            
            so.location[0] = 35 + xy[0] + ((random() - 0.5) * 3)
            so.location[1] = 25 + xy[1] + ((random() - 0.5) * 3)
            so.location[2] = 3 + (j * 5 * random())

    #so.rotation_euler[0] = radians(45) + i
