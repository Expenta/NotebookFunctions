# -*- coding: utf-8 -*-
"""
@author: Kristian Hyttel Pedersen
@email: 102928@grundfos.com
"""

def PrintToKRL(Results, AngleA, AngleB, AngleC, ActionCount, NumberOfDriveToPoints, Offset, RotList = [], Filename = "Results.txt", PointName = "Target", Debug = False):
    idx = 0
    
    if Debug:
        print(Results)
    
    # Write warning header
    print("BE VERY CAREFUL WHEN USING SPTP TO GO TO THESE POSITIONS!!! S AND T ARE 0!")
    
    if NumberOfDriveToPoints > 0:
        for i in range(ActionCount):
            PointNameTemp = PointName + str(i+1)
            PointText = "\nDECL E6POS X" + PointNameTemp + "[{}]".format(NumberOfDriveToPoints+1)
            print(PointText)
            
            AdjustedAngleA = AngleA + RotList[i*(NumberOfDriveToPoints+1)]
            
            for j in range(NumberOfDriveToPoints+1):
                Text = "X" + PointNameTemp + "[{}]={{X {:.3f}, Y {:.3f}, Z {:.3f}, A {:.3f}, B {:.3f}, C {:.3f}, S 0, T 0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}}".format(j+1,Results[idx][0][0,3] + Offset[0],Results[idx][1][0,3] + Offset[1],Results[idx][2][0,3] + Offset[2],AdjustedAngleA,AngleB,AngleC)
                print(Text)
                idx = idx + 1
        if NumberOfDriveToPoints == 1:
            print("\nSaved {} points with {} drive-to point each in {}".format(ActionCount, NumberOfDriveToPoints, Filename))
        else:
            print("\nSaved {} points with {} drive-to points each in {}".format(ActionCount, NumberOfDriveToPoints, Filename))
            
    else:
        for i in range(ActionCount+1):
            PointNameTemp = PointName + str(i+1)
            Text = "\nDECL E6POS X" + PointNameTemp + "={{X {:.3f}, Y {:.3f}, Z {:.3f}, A {:.3f}, B {:.3f}, C {:.3f}, S 0, T 0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}}".format(Results[i][0][0,3] + Offset[1],Results[i][1][0,3] + Offset[1],Results[i][2][0,3] + Offset[2],AdjustedAngleA,AngleB,AngleC)
            print(Text)
        print("\nSaved {} points in {}".format(ActionCount, Filename))