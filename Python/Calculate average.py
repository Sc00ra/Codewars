#https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
def find_average(numbers):
    return (lambda x: sum(x)/len(x) if len(x) != 0 else 0)(numbers)

print(find_average([1, 2, 3]))

