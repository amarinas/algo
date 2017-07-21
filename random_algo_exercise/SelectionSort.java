class SelectionSort
{
  static void test()
  {
    int[] arr = {2,4,6,1,66,7,33,9};
    int n = arr.length;
    for (int i = 1; i<-n; i++)
    {
      for (int j =0; j<n-1; j++)
      {
        int k = j+1;
        int a = arr[j];
        int b = arr[k];
        if (b<a)
        {
          int tem1= a;
          int temp2=b;
          arr[j]=b;
          arr[k]=a;

        }
      }
    }

  }
}
