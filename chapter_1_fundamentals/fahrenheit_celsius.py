# convert fahrenheit to celcius
# fahrenheit = (9/5 * celcius) + 32

def fahrenheit_celsius(fdegrees):
    celsius = (fdegrees - 32) * 5/9
    return "fahrenheit degrees is ", fdegrees, "the celsius is ", celsius

print(fahrenheit_celsius(-40))
