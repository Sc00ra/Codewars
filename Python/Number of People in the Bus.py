#https://www.codewars.com/kata/5648b12ce68d9daa6b000099
def number(bus_stops):
    count = 0
    for element in bus_stops:
        count += element[0]
        count -= element[1]
    return count
    