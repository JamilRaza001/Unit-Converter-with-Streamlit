# Conversion functions for different unit types

def ConvertLength(value, FromUnit, ToUnit):
    ConverstionFactors ={
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'micrometers': 1e-6,
        'nanometers': 1e-9,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254,
        'nauticalmiles': 1852

    }

    # Convert the value to meters, and then from meters to the target unit
    ValueMeter = value * ConverstionFactors[FromUnit]
    return ValueMeter / ConverstionFactors[ToUnit]
  
def ConvertTemperature(value, FromUnit, ToUnit):
    if FromUnit == "Celsius":
        if ToUnit == "Fahrenheit":
            return (value * 9/5) + 32
        elif ToUnit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif FromUnit == "Fahrenheit":
        if ToUnit == "Celsius":
            return (value - 32) * 5/9
        elif ToUnit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif FromUnit == "Kelvin":
        if ToUnit == "Celsius":
            return value - 273.15
        elif ToUnit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

def ConvertMass(value, FromUnit, ToUnit):
    ConverstionFactors = {
        "tonne": 1000,
        "kilogram": 1,
        "gram": 0.001,
        "milligram": 0.000001,
        "microgram": 1e-6,
        "imperial ton": 1016.05,
        "US ton": 907.185,
        "stone": 6.35029,
        "pound": 0.453592,
        "ounce": 0.0283495
    }
    ValueInBase = value * ConverstionFactors[FromUnit]
    return ValueInBase / ConverstionFactors[ToUnit]

def ConvertArea(value, FromUnit, ToUnit):
    ConverstionFactors = {
        "square meter": 1,
        "square kilometer": 1e6,
        "square mile": 2.59e6,
        "square yard": 0.836127,
        "square foot": 0.092903,
        "square inch": 0.00064516,
        "hectare": 10000,
        "acre": 4046.86
    }
    ValueInBase = value * ConverstionFactors[FromUnit]
    return ValueInBase / ConverstionFactors[ToUnit]

def ConvertVolume(value, FromUnit, ToUnit):
    ConverstionFactors = {
        "cubic meter": 1,
        "liter": 0.001,
        "milliliter": 0.000001,
        "cubic centimeter": 1e-6,
        "cubic inch": 1.63871e-5,
        "cubic foot": 0.0283168,
        "gallon": 0.00378541
    }
    ValueInBase = value * ConverstionFactors[FromUnit]
    return ValueInBase / ConverstionFactors[ToUnit]

# New Conversion Functions

def ConvertDigitalStorage(value, FromUnit, ToUnit):
    # Base unit is byte
    ConverstionFactors = {
        "bit": 1/8,
        "kilobit": 1024/8,
        "megabit": 1024**2/8,
        "gigabit": 1024**3/8,
        "terabit": 1024**4/8,
        "petabit": 1024**5/8,
        "byte": 1,
        "kilobyte": 1024,
        "megabyte": 1024**2,
        "gigabyte": 1024**3,
        "terabyte": 1024**4,
        "petabyte": 1024**5
    }
    ValueInBytes = value * ConverstionFactors[FromUnit]
    return ValueInBytes / ConverstionFactors[ToUnit]

def ConvertEnergy(value, FromUnit, ToUnit):
    # Base unit is Joule
    ConverstionFactors = {
        "joule": 1,
        "kilojoule": 1000,
        "gram calorie": 4.184,
        "kilocalorie": 4184,
        "watt-hour": 3600,
        "kilowatt-hour": 3600000,
        "electronvolt": 1.602176634e-19
    }
    ValueInJoules = value * ConverstionFactors[FromUnit]
    return ValueInJoules / ConverstionFactors[ToUnit]

def ConvertFrequency(value, FromUnit, ToUnit):
    # Base unit is Hertz
    ConverstionFactors = {
        "hertz": 1,
        "kilohertz": 1e3,
        "megahertz": 1e6,
        "gigahertz": 1e9
    }
    ValueInHZ = value * ConverstionFactors[FromUnit]
    return ValueInHZ / ConverstionFactors[ToUnit]

def ConvertSpeed(value, FromUnit, ToUnit):
    # Base unit is meter per second
    ConverstionFactors = {
        "meter per second": 1,
        "kilometer per hour": 0.27778,  # 1 km/h = 0.27778 m/s
        "mile per hour": 0.44704,         # 1 mph = 0.44704 m/s
        "foot per second": 0.3048,        # 1 ft/s = 0.3048 m/s
        "knot": 0.514444                  # 1 knot = 0.514444 m/s
    }
    ValueInMPS = value * ConverstionFactors[FromUnit]
    return ValueInMPS / ConverstionFactors[ToUnit]

def ConvertTime(value, FromUnit, ToUnit):
    # Base unit is second
    ConverstionFactors = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800
    }
    ValueInSeconds = value * ConverstionFactors[FromUnit]
    return ValueInSeconds / ConverstionFactors[ToUnit]
