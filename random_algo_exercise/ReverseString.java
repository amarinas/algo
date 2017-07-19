
import java.util.Scanner;

class ReverseString{
  public static void main(String args[]){
    String original, reverse = "";
    Scanner sc = new Scanner(System.in);
    original = sc.nextLine();

    for (int i = original.length() -1; i >=0; i--){
      reverse += original.charAt(i);
    }
    System.out.println("reverse input of the string = " + reverse);
  }
}
