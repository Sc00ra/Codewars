#https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a, b):
    
    indexes = []
    for i in range(len(a)):
        if a[i] in b:
            indexes.append(i)
            
    print(indexes)
    i=0
    for index in indexes:
       a.pop(index-i)
       i+=1 

    return a

print(array_diff([1,2,2], [2]))
