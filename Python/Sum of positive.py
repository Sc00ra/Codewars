# https://www.codewars.com/kata/5715eaedb436cf5606000381

def positive_sum(arr):
  suma=0
  for element in arr: 
    if element > 0:
      suma += element
  return suma