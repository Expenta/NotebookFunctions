# -*- coding: utf-8 -*-
"""
@author: Kristian Hyttel Pedersen
@email: 102928@grundfos.com
"""

import math

def CalcRotatedPos(TransformationMatrix, angle = 0, OriginX = 0, OriginY = 0): # Calculate position of new point given a certain rotation around the origin
    x = TransformationMatrix[0,3]
    y = TransformationMatrix[1,3]
    
    # Translate back to origin
    x -= OriginX
    y -= OriginY
    
    # Rotate
    s = math.sin(math.radians(angle))
    c = math.cos(math.radians(angle))

    newx = x*c - y*s
    newy = x*s + y*c
    
    # Translate back to original location
    newx += OriginX
    newy += OriginY
    
    TransformationMatrix[0,3] = newx
    TransformationMatrix[1,3] = newy
    
    return TransformationMatrix

def CalcRotatedPosAroundAxis(TransformationMatrix, axis, angle = 0, OriginX = 0, OriginY = 0, OriginZ = 0): # Calculate position of new point given a certain rotation around the origin

    if axis == 'X' or axis == 'x':
        z = TransformationMatrix[2,3]
        y = TransformationMatrix[1,3]
        
        # Translate back to origin
        z -= OriginZ
        y -= OriginY
        
        # Rotate
        s = math.sin(math.radians(angle))
        c = math.cos(math.radians(angle))
        
        # print("Sin: {}".format(s))
        # print("Cos: {}".format(c))
        
        newz = z*c + y*s
        newy = z*-s + y*c
        
        # Translate back to original location
        newz += OriginZ
        newy += OriginY
        
        TransformationMatrix[2,3] = newz
        TransformationMatrix[1,3] = newy
        
        # print("Newz: {}".format(newz))
        # print("Newy: {}".format(newy))
        
    elif axis == 'Y' or axis == 'y':
        x = TransformationMatrix[0,3]
        z = TransformationMatrix[2,3]
        
        # Translate back to origin
        x -= OriginX
        z -= OriginZ
        
        # Rotate
        s = math.sin(math.radians(angle))
        c = math.cos(math.radians(angle))
    
        newx = x*c - z*-s
        newz = x*-s + z*c
        
        # Translate back to original location
        newx += OriginX
        newz += OriginZ
        
        TransformationMatrix[0,3] = newx
        TransformationMatrix[2,3] = newz
        
        # print("Newx: {}".format(newx))
        # print("Newz: {}".format(newz))
        
    elif axis == 'Z' or axis == 'z':
        x = TransformationMatrix[0,3]
        y = TransformationMatrix[1,3]
        
        # Translate back to origin
        x -= OriginX
        y -= OriginY
        
        # Rotate
        s = math.sin(math.radians(angle))
        c = math.cos(math.radians(angle))
    
        newx = x*c - y*s
        newy = x*s + y*c
        
        # Translate back to original location
        newx += OriginX
        newy += OriginY
        
        TransformationMatrix[0,3] = newx
        TransformationMatrix[1,3] = newy
        
        # print("Newx: {}".format(newx))
        # print("Newy: {}".format(newy))
    
    return TransformationMatrix