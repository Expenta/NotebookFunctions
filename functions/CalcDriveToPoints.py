# -*- coding: utf-8 -*-
"""
@author: Kristian Hyttel Pedersen
@email: 102928@grundfos.com
"""

from functions.TranslateLocal import TranslateLocal
from functions.TranslateGlobal import TranslateGlobal
from functions.PrintMatrix import PrintMatrix

def CalcDriveToPoints(TransformationMatrix, NumberOfDriveToPoints, DriveToZ, DriveToFrame = 1, DriveToX = 0, DriveToY = 0, Debug = False):
    if DriveToX != 0 or DriveToY != 0 or DriveToZ != 0:
        Results = []
        
        TranslateDistanceX = DriveToX / NumberOfDriveToPoints
        TranslateDistanceY = DriveToY / NumberOfDriveToPoints
        TranslateDistanceZ = DriveToZ / NumberOfDriveToPoints
        
        if Debug:
            PrintMatrix(TransformationMatrix, "TransformationMatrix parsed to CalcDriveToPoints.py: ")
        
        for i in range(NumberOfDriveToPoints):
            if Debug:
                print("\nCalculating DriveToPoint number {}: ".format(i+1))

            if DriveToFrame == 1: # Local coordinate frame
                TransformationMatrix = TranslateLocal(TransformationMatrix.copy(), TranslateDistanceX, TranslateDistanceY, TranslateDistanceZ, Debug=Debug)

            elif DriveToFrame == 2: # Global coordinate frame
                TransformationMatrix = TranslateGlobal(TransformationMatrix.copy(), TranslateDistanceX, TranslateDistanceY, TranslateDistanceZ, Debug=Debug)
            
            Results.append(TransformationMatrix.copy())
        
    return Results
            