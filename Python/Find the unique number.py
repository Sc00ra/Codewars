# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
def find_uniq(arr):
    arr = sorted(arr)
    if arr[0] == arr[1]: return arr[-1]
    else:                return arr[0]


print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))