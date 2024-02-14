# -*- coding: utf-8 -*-
"""
@author: Kristian Hyttel Pedersen
@email: 102928@grundfos.com
"""

def GetInput(text, ValueDataType, upperlimit = None, lowerlimit = None):
    value = input(text)
    
    while True:
        isBool = False
        isInt = False
        isFloat = False
        
        if ValueDataType == "bool":
            try:
                bool(value)
            except:
                value = input("Invalid input. Choose either Yes or No: ")
            else:
                isBool = True
                # print("isBool: {}".format(isBool))

        elif ValueDataType == "int":
            try:
                int(value)
            except:
                value = input("Invalid input. Input is not a whole number: ")
            else:
                isInt = True
                # print("isInt: {}".format(isInt))

        elif ValueDataType == "float":
            try:
                float(value)
            except:
                value = input("Invalid input. Input is not a number: ")
            else:
                isFloat = True
                # print("isFloat: {}".format(isFloat))

        else:
            print("PROGRAM ERROR. ValueDataType FOR 'CheckInput' FUNCTION NOT PROGRAMMED!")
        
        if isBool:
            if value == "0" or value == "n" or value == "N" or value == "no" or value == "No" or value == "NO":
                value = False
                break
            elif value == "1" or value == "y" or value == "Y" or value == "yes" or value == "Yes" or value == "YES":
                value = True
                break
            else:
                value = input("Invalid input. Choose either Yes or No: ")
                
        elif isInt:
            value = int(value)
            if lowerlimit != None and value < lowerlimit:
                value = input("Invalid input. Input exceeds limit of {}. Enter new value: ".format(lowerlimit))
            elif upperlimit != None and value > upperlimit:
                value = input("Invalid input. Input exceeds limit of {}. Enter new value: ".format(upperlimit))
            else:
                break
                
        elif isFloat:
            value = float(value)
            if lowerlimit != None and value < lowerlimit:
                value = input("Invalid input. Input exceeds limit of {}. Enter new value: ".format(lowerlimit))
            elif upperlimit != None and value > upperlimit:
                value = input("Invalid input. Input exceeds limit of {}. Enter new value: ".format(upperlimit))
            else:
                break
    
    return value