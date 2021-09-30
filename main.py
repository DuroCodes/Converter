from os import system as sys
from termcolor import colored as c
from time import sleep

sys("clear")

title = """ ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗ 
██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝
██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝"""
title = title.split("\n")
print(c(title[0],"red"))
print(c(title[1],"yellow"))
print(c(title[2],"green"))
print(c(title[3],"cyan"))
print(c(title[4],"blue"))
print(c(title[5],"magenta"))


VALUE = float(input("Enter the number you wish to convert (Example: 10): "))
UNIT1 = input("\nWhich unit do you want to convert it from (Example: feet): ")
UNIT2 = input("Which unit do you want to convert it to (Example: inches): ")

class lengths:
    # Metric lengths
    KILOMETER_LIST = ["km", "kilom", "kilomet", "kilometer", "kmeter", "kilometers", "kms"]
    METER_LIST = ["m", "me", "met", "mete", "meter", "meters", "ms"]
    CENTIMETER_LIST = ["cm", "centim", "centime", "cmeter", "centimeter", "cms", "centimeters"]
    MILLIMETER_LIST = ["mm", "mms", "millimeter", "millimeters", "mmeter", "mmeters"]
    # Imperial lengths
    MILE_LIST = ["mi", "mis", "mil", "mils", "mile", "miles"]
    YARD_LIST = ["y", "ys", "ya", "yar", "yards", "yard"]
    FEET_LIST = ["ft", "feet", "foot", "fts"]
    INCH_LIST = ["in", "inc", "inch", "inches"]
class weights:
    # Metric weights
    METRIC_TON_LIST = ["mt", "mts", "metric ton", "metric tons"]
    KILOGRAM_LIST = ["kg", "kgs", "kilogram", "kilograms", "kgram", "kgrams"]
    GRAM_LIST = ["g", "gs", "gram", "grams"]
    MILLIGRAM_LIST = ["mg", "mgs", "milligram", "milligrams", "mgram", "mgrams"]
    # Imperial weights
    TON_LIST = ["t", "ton", "ts", "tons"]
    POUND_LIST = ["lb", "lbs", "pound", "pounds"]
    OUNCE_LIST = ["oz", "ozs", "ounce", "ounces"]

class LENGTH_CONVERTERS:
    def kilometer_convert(value, unit):
        if unit in lengths.METER_LIST: conversionFactor = 1000
        elif unit in lengths.CENTIMETER_LIST: conversionFactor = 100000
        elif unit in lengths.MILLIMETER_LIST: conversionFactor = 100000
        elif unit in lengths.MILE_LIST: conversionFactor = 0.621371
        elif unit in lengths.YARD_LIST: conversionFactor = 1093.61
        elif unit in lengths.FEET_LIST: conversionFactor = 3280.84
        elif unit in lengths.INCH_LIST: conversionFactor = 39370.1
        return value*conversionFactor
    
    def meter_convert(value, unit):
        if unit in lengths.KILOMETER_LIST: conversionFactor = 0.001
        elif unit in lengths.CENTIMETER_LIST: conversionFactor = 100
        elif unit in lengths.MILLIMETER_LIST: conversionFactor = 1000
        elif unit in lengths.MILE_LIST: conversionFactor = 0.000621371
        elif unit in lengths.YARD_LIST: conversionFactor = 1.09361
        elif unit in lengths.FEET_LIST: conversionFactor = 3.28084
        elif unit in lengths.INCH_LIST: conversionFactor = 39.3701
        return value*conversionFactor

    def centimeter_convert(value, unit):
        if unit in lengths.KILOMETER_LIST: conversionFactor = 10000
        elif unit in lengths.METER_LIST: conversionFactor = 0.01
        elif unit in lengths.MILLIMETER_LIST: conversionFactor = 10
        elif unit in lengths.MILE_LIST: conversionFactor = 0.00000621371
        elif unit in lengths.YARD_LIST: conversionFactor = 0.0109361
        elif unit in lengths.FEET_LIST: conversionFactor = 0.0328084
        elif unit in lengths.INCH_LIST: conversionFactor = 0.393701
        return value*conversionFactor
    
    def millimeter_convert(value, unit):
        if unit in lengths.KILOMETER_LIST: conversionFactor = 0.000001
        elif unit in lengths.METER_LIST: conversionFactor = 0.001
        elif unit in lengths.CENTIMETER_LIST: conversionFactor = 0.1
        elif unit in lengths.MILE_LIST: conversionFactor = 0.000000621371
        elif unit in lengths.YARD_LIST: conversionFactor = 0.00109361
        elif unit in lengths.FEET_LIST: conversionFactor = 0.00328084
        elif unit in lengths.INCH_LIST: conversionFactor = 0.0393701
        return value*conversionFactor

    def mile_convert(value, unit):
        if unit in lengths.KILOMETER_LIST: conversionFactor = 1.60934
        elif unit in lengths.METER_LIST: conversionFactor = 1609.34
        elif unit in lengths.CENTIMETER_LIST: conversionFactor = 160934
        elif unit in lengths.MILLIMETER_LIST: conversionFactor = 1609340
        elif unit in lengths.YARD_LIST: conversionFactor = 1760
        elif unit in lengths.FEET_LIST: conversionFactor = 5280
        elif unit in lengths.INCH_LIST: conversionFactor = 63360
        return value*conversionFactor
    
    def yard_convert(value, unit):
        if unit in lengths.KILOMETER_LIST: conversionFactor = 0.0009144
        elif unit in lengths.METER_LIST: conversionFactor = 0.9144
        elif unit in lengths.CENTIMETER_LIST: conversionFactor = 91.44
        elif unit in lengths.MILLIMETER_LIST: conversionFactor = 914.4
        elif unit in lengths.MILE_LIST: conversionFactor = 0.000568182
        elif unit in lengths.FEET_LIST: conversionFactor = 3
        elif unit in lengths.INCH_LIST: conversionFactor = 36
        return value*conversionFactor

    def feet_convert(value, unit):
        if unit in lengths.KILOMETER_LIST: conversionFactor = 0.0003048
        elif unit in lengths.METER_LIST: conversionFactor = 0.3048
        elif unit in lengths.CENTIMETER_LIST: conversionFactor = 30.48
        elif unit in lengths.MILLIMETER_LIST: conversionFactor = 304.8
        elif unit in lengths.MILE_LIST: conversionFactor = 0.000189394
        elif unit in lengths.YARD_LIST: conversionFactor = 0.333333
        elif unit in lengths.INCH_LIST: conversionFactor = 12
        return value*conversionFactor

    def inch_convert(value, unit):
        if unit in lengths.KILOMETER_LIST: conversionFactor = 0.00002540005
        elif unit in lengths.METER_LIST: conversionFactor = 0.0254
        elif unit in lengths.CENTIMETER_LIST: conversionFactor = 2.54
        elif unit in lengths.MILLIMETER_LIST: conversionFactor = 25.4
        elif unit in lengths.MILE_LIST: conversionFactor = 0.00001578282
        elif unit in lengths.YARD_LIST: conversionFactor = 0.0277778
        elif unit in lengths.FEET_LIST: conversionFactor = 0.0833333
        return value*conversionFactor
class WEIGHT_CONVERTERS:
    def metric_ton_convert(value, unit):
        if unit in weights.KILOGRAM_LIST: conversionFactor = 1000 
        elif unit in weights.GRAM_LIST: conversionFactor = 1000000
        elif unit in weights.MILLIGRAM_LIST: conversionFactor = 1000000000
        elif unit in weights.TON_LIST: conversionFactor = 1.10231
        elif unit in weights.POUND_LIST: conversionFactor = 2204.62
        elif unit in weights.OUNCE_LIST: conversionFactor = 35274  
        return value*conversionFactor 

    def kilogram_convert(value, unit):
        if unit in weights.METRIC_TON_LIST: conversionFactor = 0.001
        elif unit in weights.GRAM_LIST: conversionFactor = 1000
        elif unit in weights.MILLIGRAM_LIST: conversionFactor = 1000000
        elif unit in weights.TON_LIST: conversionFactor = 0.00110231
        elif unit in weights.POUND_LIST: conversionFactor = 2.20462
        elif unit in weights.OUNCE_LIST: conversionFactor = 35.2739199982575  
        return value*conversionFactor 

    def gram_convert(value, unit):
        if unit in weights.METRIC_TON_LIST: conversionFactor = 0.000001
        elif unit in weights.KILOGRAM_LIST: conversionFactor = 0.001
        elif unit in weights.MILLIGRAM_LIST: conversionFactor = 1000
        elif unit in weights.TON_LIST: conversionFactor = 0.0000011023
        elif unit in weights.POUND_LIST: conversionFactor = 0.00220462
        elif unit in weights.OUNCE_LIST: conversionFactor = 0.035274  
        return value*conversionFactor 

    def milligram_convert(value, unit):
        if unit in weights.METRIC_TON_LIST: conversionFactor = 0.000000001
        elif unit in weights.KILOGRAM_LIST: conversionFactor = 0.000001
        elif unit in weights.GRAM_LIST: conversionFactor = 0.001
        elif unit in weights.TON_LIST: conversionFactor = 0.00000000110231
        elif unit in weights.POUND_LIST: conversionFactor = 0.00000220462
        elif unit in weights.OUNCE_LIST: conversionFactor = 0.000035274  
        return value*conversionFactor 

    def ton_convert(value, unit):
        if unit in weights.METRIC_TON_LIST: conversionFactor = 0.907185
        elif unit in weights.KILOGRAM_LIST: conversionFactor = 907.185
        elif unit in weights.GRAM_LIST: conversionFactor = 907185
        elif unit in weights.MILLIGRAM_LIST: conversionFactor = 907200000
        elif unit in weights.POUND_LIST: conversionFactor = 2000
        elif unit in weights.OUNCE_LIST: conversionFactor = 0.000035274  
        return value*conversionFactor 

    def pound_convert(value, unit):
        if unit in weights.METRIC_TON_LIST: conversionFactor = 0.000453592
        elif unit in weights.KILOGRAM_LIST: conversionFactor = 0.453592
        elif unit in weights.GRAM_LIST: conversionFactor = 453.592
        elif unit in weights.MILLIGRAM_LIST: conversionFactor = 453592
        elif unit in weights.TON_LIST: conversionFactor = 0.0005
        elif unit in weights.OUNCE_LIST: conversionFactor = 16  
        return value*conversionFactor 

    def ounce_convert(value, unit):
        if unit in weights.METRIC_TON_LIST: conversionFactor = 0.000453592
        elif unit in weights.KILOGRAM_LIST: conversionFactor = 0.453592
        elif unit in weights.GRAM_LIST: conversionFactor = 453.592
        elif unit in weights.MILLIGRAM_LIST: conversionFactor = 453592
        elif unit in weights.TON_LIST: conversionFactor = 0.0005
        elif unit in weights.OUNCE_LIST: conversionFactor = 16  
        return value*conversionFactor 

sys("clear")

if UNIT1 in lengths.KILOMETER_LIST: print(f"\nCalculated length: {LENGTH_CONVERTERS.kilometer_convert(VALUE, UNIT2)}")
elif UNIT1 in lengths.METER_LIST: print(f"\nCalculated length: {LENGTH_CONVERTERS.meter_convert(VALUE, UNIT2)}")
elif UNIT1 in lengths.CENTIMETER_LIST: print(f"\nCalculated length: {LENGTH_CONVERTERS.centimeter_convert(VALUE, UNIT2)}")
elif UNIT1 in lengths.MILLIMETER_LIST: print(f"\nCalculated length: {LENGTH_CONVERTERS.millimeter_convert(VALUE, UNIT2)}")
elif UNIT1 in lengths.MILE_LIST: print(f"\nCalculated length: {LENGTH_CONVERTERS.mile_convert(VALUE, UNIT2)}")
elif UNIT1 in lengths.YARD_LIST: print(f"\nCalculated length: {LENGTH_CONVERTERS.yard_convert(VALUE, UNIT2)}")
elif UNIT1 in lengths.FEET_LIST: print(f"\nCalculated length: {LENGTH_CONVERTERS.feet_convert(VALUE, UNIT2)}")
elif UNIT1 in lengths.INCH_LIST: print(f"\nCalculated length: {LENGTH_CONVERTERS.inch_convert(VALUE, UNIT2)}")

elif UNIT1 in weights.METRIC_TON_LIST: print(f"\nCalculated weight: {WEIGHT_CONVERTERS.metric_ton_convert(VALUE, UNIT2)}")
elif UNIT1 in weights.KILOGRAM_LIST: print(f"\nCalculated weight: {WEIGHT_CONVERTERS.kilogram_convert(VALUE, UNIT2)}")
elif UNIT1 in weights.GRAM_LIST: print(f"\nCalculated weight: {WEIGHT_CONVERTERS.gram_convert(VALUE, UNIT2)}")
elif UNIT1 in weights.MILLIGRAM_LIST: print(f"\nCalculated weight: {WEIGHT_CONVERTERS.milligram_convert(VALUE, UNIT2)}")
elif UNIT1 in weights.TON_LIST: print(f"\nCalculated weight: {WEIGHT_CONVERTERS.ton_convert(VALUE, UNIT2)}")
elif UNIT1 in weights.POUND_LIST: print(f"\nCalculated weight: {WEIGHT_CONVERTERS.pound_convert(VALUE, UNIT2)}")
elif UNIT1 in weights.OUNCE_LIST: print(f"\nCalculated weight: {WEIGHT_CONVERTERS.ounce_convert(VALUE, UNIT2)}")

else:
    print(c("There was an error", "red"))
