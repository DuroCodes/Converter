from os import system as sys

sys("clear")

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
    INCHES_LIST = ["in", "inc", "inch", "inches"]
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

def metric_ton_convert(value, unit):
    if unit in weights.KILOGRAM_LIST: conversionFactor = 1000 
    if unit in weights.GRAM_LIST: conversionFactor = 1000000
    if unit in weights.MILLIGRAM_LIST: conversionFactor = 1000000000
    if unit in weights.TON_LIST: conversionFactor = 1.10231
    if unit in weights.POUND_LIST: conversionFactor = 2204.62
    if unit in weights.OUNCE_LIST: conversionFactor = 35274  
    return value*conversionFactor 
def kilogram_convert(value, unit):
    if unit in weights.METRIC_TON_LIST: conversionFactor = 0.001
    if unit in weights.GRAM_LIST: conversionFactor = 1000
    if unit in weights.MILLIGRAM_LIST: conversionFactor = 1000000
    if unit in weights.TON_LIST: conversionFactor = 0.00110231
    if unit in weights.POUND_LIST: conversionFactor = 2.20462
    if unit in weights.OUNCE_LIST: conversionFactor = 35.2739199982575  
    return value*conversionFactor 
def gram_convert(value, unit):
    if unit in weights.METRIC_TON_LIST: conversionFactor = 0.000001
    if unit in weights.KILOGRAM_LIST: conversionFactor = 0.001
    if unit in weights.MILLIGRAM_LIST: conversionFactor = 1000
    if unit in weights.TON_LIST: conversionFactor = 0.0000011023
    if unit in weights.POUND_LIST: conversionFactor = 0.00220462
    if unit in weights.OUNCE_LIST: conversionFactor = 0.035274  
    return value*conversionFactor 
def milligram_convert(value, unit):
    if unit in weights.METRIC_TON_LIST: conversionFactor = 0.000000001
    if unit in weights.KILOGRAM_LIST: conversionFactor = 0.000001
    if unit in weights.GRAM_LIST: conversionFactor = 0.001
    if unit in weights.TON_LIST: conversionFactor = 0.00000000110231
    if unit in weights.POUND_LIST: conversionFactor = 0.00000220462
    if unit in weights.OUNCE_LIST: conversionFactor = 0.000035274  
    return value*conversionFactor 
def ton_convert(value, unit):
    if unit in weights.METRIC_TON_LIST: conversionFactor = 0.907185
    if unit in weights.KILOGRAM_LIST: conversionFactor = 907.185
    if unit in weights.GRAM_LIST: conversionFactor = 907185
    if unit in weights.MILLIGRAM_LIST: conversionFactor = 907200000
    if unit in weights.POUND_LIST: conversionFactor = 2000
    if unit in weights.OUNCE_LIST: conversionFactor = 0.000035274  
    return value*conversionFactor 
