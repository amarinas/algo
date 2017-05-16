# convert celsius to fahrenheit

def celsius_fahrenheit(cdegrees):
    fahrenheit = 32 + (cdegrees * 9/5) 
    return "celsius degrees is ", cdegrees, "the fahrenheit is ", fahrenheit

print(celsius_fahrenheit(-40))
