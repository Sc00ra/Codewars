#https://www.codewars.com/kata/51fc12de24a9d8cb0e000001
def valid_ISBN10(isbn): 
    if len(isbn) != 10:
        return False
    result = 0

    for i in range(0,len(isbn)):
        try:
            if i>=0 and i<9:
                if isbn[i] == "X":
                    return False
                else:
                    result += int(isbn[i])*(i+1)
            else: 
                if isbn[i] == "X":
                    result += 10*(i+1)
                
                else:
                    result += int(isbn[i])*(i+1)
        except ValueError:
            return False
    if result % 11 == 0:
        return True
    return False

print(valid_ISBN10('X123456788'))



 