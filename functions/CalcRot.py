# -*- coding: utf-8 -*-
"""
@author: Kristian Hyttel Pedersen
@email: 102928@grundfos.com
"""

import numpy as np
import math

def CalcRot(TransformationMatrix, AngleC, AngleB, AngleA, Debug = False):
    
    RC = np.matrix([[1,0,0,0],[0,math.cos(math.radians(AngleC)),-math.sin(math.radians(AngleC)),0],[0,math.sin(math.radians(AngleC)),math.cos(math.radians(AngleC)),0],[0,0,0,1]],dtype=float)
    RB = np.matrix([[math.cos(math.radians(AngleB)),0,math.sin(math.radians(AngleB)),0],[0,1,0,0],[-math.sin(math.radians(AngleB)),0,math.cos(math.radians(AngleB)),0],[0,0,0,1]],dtype=float)
    RA = np.matrix([[math.cos(math.radians(AngleA)),-math.sin(math.radians(AngleA)),0,0],[math.sin(math.radians(AngleA)),math.cos(math.radians(AngleA)),0,0],[0,0,1,0],[0,0,0,1]],dtype=float)
    
    ResultTemp = RC*TransformationMatrix
    ResultTemp = RB*ResultTemp
    ResultTemp = RA*ResultTemp
    
    ResultTemp[0,3] = TransformationMatrix[0,3]
    ResultTemp[1,3] = TransformationMatrix[1,3]
    ResultTemp[2,3] = TransformationMatrix[2,3]
    Result = ResultTemp
    
    if Debug:
        print("\nDesired rotation: X: {:.3f} deg, Y: {:.3f} deg, Z: {:.3f} deg".format(AngleC, AngleB, AngleA))
        
        r11 = Result[0,0]
        r12 = Result[0,1]
        r13 = Result[0,2]
        r21 = Result[1,0]
        r22 = Result[1,1]
        r23 = Result[1,2]
        r31 = Result[2,0]
        r21 = Result[2,1]
        r33 = Result[2,2]
        
        theta1 = np.arctan(-r23 / r33)
        theta2 = np.arctan(r13 * np.cos(theta1) / r33)
        theta3 = np.arctan(-r12 / r11)
        
        print("Reverse calculation of current rotation matrix: RX: {:.3f}, RY: {:.3f}, RZ: {:.3f}".format(math.degrees(theta1), math.degrees(theta2), math.degrees(theta3)))
    
    return Result