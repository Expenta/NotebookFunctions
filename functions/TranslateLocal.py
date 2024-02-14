# -*- coding: utf-8 -*-
"""
@author: Kristian Hyttel Pedersen
@email: 102928@grundfos.com
"""

import numpy as np
from functions.PrintMatrix import PrintMatrix

def TranslateLocal(TransformationMatrix, DistanceX = 0, DistanceY = 0, DistanceZ = 0, Debug = False):
    if Debug:
        PrintMatrix(TransformationMatrix, "TransformationMatrix parsed to TranslateLocal: ")
    TranslationVector = np.matrix([[DistanceX],[DistanceY],[DistanceZ],[1]])
    TranslationVector = TransformationMatrix*TranslationVector
    
    DifferenceX = TranslationVector[0,0] - TransformationMatrix[0,3]
    DifferenceY = TranslationVector[1,0] - TransformationMatrix[1,3]
    DifferenceZ = TranslationVector[2,0] - TransformationMatrix[2,3]
    
    TransformationMatrix[0,3] = TranslationVector[0]
    TransformationMatrix[1,3] = TranslationVector[1]
    TransformationMatrix[2,3] = TranslationVector[2]
    
    if Debug:
        print("\nDesired Translation on X-axis: {:.3f}mm".format(DistanceX))
        print("Desired Translation on Y-axis: {:.3f}mm".format(DistanceY))
        print("Desired Translation on Z-axis: {:.3f}mm".format(DistanceZ))
        
        print("\nCalculated Translation on X-axis: {}mm".format(DifferenceX))
        print("Calculated Translation on Y-axis: {:.3f}mm".format(DifferenceY))
        print("Calculated Translation on Z-axis: {:.3f}mm".format(DifferenceZ))
        PrintMatrix(TransformationMatrix, "TransformationMatrix after TranslateLocal: ")
    
    return TransformationMatrix