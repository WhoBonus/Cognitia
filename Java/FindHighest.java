//package mypack;

public class FindHighest {
    public static void main (String [] args) {
        int[] nums = {10, 0, 2, 50, 30}; //20
        int max = findMax(nums);
        System.out.println("Max is: " + max);
    }

    //main method was static so everything in static context called must be static as well. Default access modifier 
    private static int findMax(int[] nums) {
        //int max = Integer.MIN_VALUE;
        int max = 0;
        for (int i =0; i < nums.length; i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
        }
            
        return max;
    }
}