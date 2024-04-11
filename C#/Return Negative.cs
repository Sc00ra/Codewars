//https://www.codewars.com/kata/55685cd7ad70877c23000102

using System;

public static class Kata
{
  public static int MakeNegative(int number)
  {
    if(number >= 0){
        return number - (2*number);
    }   
    
    return number;
    
  }
}