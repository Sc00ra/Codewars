#https://www.codewars.com/kata/57eaeb9578748ff92a000009

def sum_mix(arr):
    sums=0
    for element in arr:
        
        if isinstance(element,int):
            sums+=element
        else:
            sums+=int(element)
    return sums
    
print(sum_mix([9, 3, '7', '3']))
