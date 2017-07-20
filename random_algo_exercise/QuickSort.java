import java.util.*;
import java.io.*;
import java.math.*;
import java.util.regex.*;

public class QuickSort{
  public static void quicksort(int [] array){
    quicksort(array, 0, array.length -1);

  }
  public static void quicksort(int[] array, int left, int right){
    if (left >= right){
      return;
    }
    int pivot = array[(left +right) / 2 ];
    int index = partition(array, left, right, pivot);
    quicksort(array, left, index - 1);
    quicksort(array, index, right);

  }



  public static int partition(int[] array, int left, int right, int pivot){
    while(left <= right){
      while(array[left] <= pivot){
        left ++;
      }
      while (array[right]> pivot){
        right --;
      }
      if (left <= right){
        int temp =0;
        temp= array[right];
        array[right]= array[left];
        array[left]= temp;
      }
    }
    return left;
  }
}


// public static void main (String[] args){
//   Quicksort sort = new Quicksort();
//   sort.quicksort([44,33,4,2,8,23,55,99])
//
// }
