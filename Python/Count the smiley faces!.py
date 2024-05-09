#https://www.codewars.com/kata/583203e6eb35d7980400002a

def count_smileys(arr):
    count =0 
    good = [":)",":-)",":~)",":D",":-D",":~D",";)",";-)",";~)",";D",";-D",";~D"]
    for element in arr:
        if element in good:
            count+=1
    return count