#https://www.codewars.com/kata/5282b48bb70058e4c4000fa7

def hex_string_to_RGB(hex_string): 
    hex_string = hex_string.lower()[1:]
    i = 0
    rgb = []
    while i < len(hex_string):
        hex = hex_string[i] + hex_string[i+1]
        rgb.append(int(hex,16))
        i+=2
    return {'r':rgb[0], 'g':rgb[1],'b':rgb[2]}
    

print(hex_string_to_RGB("#FF9933"))