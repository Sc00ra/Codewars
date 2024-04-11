#https://www.codewars.com/kata/546e2562b03326a88e000020
def square_digits(num):
    # Your code here
    num_str = str(num)
    final = ''
    for element in num_str:
        
        number = int(element)**2
        print(number)
        number = str(number)
        final  = final + number
    final = int(final)
 
    return final