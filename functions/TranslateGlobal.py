# -*- coding: utf-8 -*-
"""
@author: Kristian Hyttel Pedersen
@email: 102928@grundfos.com
"""

from functions.PrintMatrix import PrintMatrix

def TranslateGlobal(TransformationMatrix, DistanceX = 0, DistanceY = 0, DistanceZ = 0, Debug = False):
    TransformationMatrix[0,3] = TransformationMatrix[0,3] + DistanceX
    TransformationMatrix[1,3] = TransformationMatrix[1,3] + DistanceY
    TransformationMatrix[2,3] = TransformationMatrix[2,3] + DistanceZ
    
    if Debug:
        PrintMatrix(TransformationMatrix, "TransformationMatrix after TranslateGlobal: ")
    
    return TransformationMatrix