#https://www.codewars.com/kata/54ba84be607a92aa900000f1
def is_isogram(string):
    #your code here
    
    string = string.lower().strip()
    print(string)
    
    x=[0 for _ in range(len(string))]
    print(x)
    for element in string: 
        for j in range(0,len(string)):
            if string[j] == element:
                x[j] = x[j] + 1
    for element in x:
        if element > 1:
            return False
    return True