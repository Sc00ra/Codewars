//https://www.codewars.com/kata/515e271a311df0350d00000f

public static class Kata
{
  public static int SquareSum(int[] numbers)
  { 
    int sum = 0;
    foreach(int element in numbers){
        sum += element*element;
    }   
    return sum;
  }
}