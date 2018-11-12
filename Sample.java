public class ArrayAverage{
   public static void main(String [] args){
      int[] ok = {4,7,9,5,2};
      averageArray(ok);
   }
   public static void averageArray(int[] n){
      int sum = 0;
      int average;
      for(int i = 0; i < n.length; i++){
         sum += n[i];  
      }
      
      average = sum/n.length;
      System.out.println(average);
   }
}