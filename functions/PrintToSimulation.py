# -*- coding: utf-8 -*-
"""
@author: Kristian Hyttel Pedersen
@email: 102928@grundfos.com
"""

import os
import pandas as pd
import warnings

def PrintToSimulation(Results, AngleA, AngleB, AngleC, ActionCount, NumberOfDriveToPoints, Offset, RotList = [], Filename = "Results.txt", PointName = "Target", Debug = False):
    warnings.filterwarnings('ignore')
    
    TagGroupName = Filename
    Path = "results/"
    Filename = Path + Filename + "Results.xls"
    
    if os.path.isfile(Filename):
        os.remove(Filename)
    
    Size = len(Results)
    Empty = [None] * (Size+1)
    
    TagNames = Empty.copy()
    TagIndexes = Empty.copy()
    TagSuffix = Empty.copy()
    XCoords = Empty.copy()
    YCoords = Empty.copy()
    ZCoords = Empty.copy()
    AnglesA = Empty.copy()
    AnglesB = Empty.copy()
    AnglesC = Empty.copy()
    
    TagNames[0] = 'Tag Prefix'
    TagIndexes[0] = 'Tag Index'
    TagSuffix[0] = 'Tag Suffix'
    XCoords[0] = 'X(mm)'
    YCoords[0] = 'Y(mm)'
    ZCoords[0] = 'Z(mm)'
    AnglesA[0] = 'Roll(deg)'
    AnglesB[0] = 'Pitch(deg)'
    AnglesC[0] = 'Yaw(deg)'
    
    for j in range(1,Size+1):
        TagNames[j] = 'Tag'
        TagIndexes[j] = j
        TagSuffix[j] = ''
        
    for j in range(Size):
        XCoords[j+1] = Results[j][0][0,3] + Offset[0]
        YCoords[j+1] = Results[j][1][0,3] + Offset[1]
        ZCoords[j+1] = Results[j][2][0,3] + Offset[2]
        if RotList == []:
            AnglesA[j+1] = AngleA
        else:
            AnglesA[j+1] = AngleA + RotList[j]        
        AnglesB[j+1] = AngleB
        AnglesC[j+1] = AngleC
    
    df = pd.DataFrame({'TagGroup Name :': TagNames, TagGroupName: TagIndexes, 'Reference:': TagSuffix, 'Global': XCoords, 'Temp1': YCoords, 'Temp2': ZCoords, 'Temp3': AnglesC, 'Temp4': AnglesB, 'Temp5': AnglesA})
    
    print("\n\n")
    print(df)

    if Debug:
        print("\n\n")
        print(df)
    
    # df.to_excel(Filename, sheet_name='sheet1', index=False)
    
    print("\nSaved {} tags in {}".format(Size, Filename))