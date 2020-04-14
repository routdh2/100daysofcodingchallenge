/**
* Problem Statement: https://leetcode.com/problems/sum-of-two-integers
*/
class Solution {
    public int getSum(int a, int b) {
        int carry;
        while(b!=0) { //While carry!=0 -> meaning loop over till there is carry
            carry=a&b; //a&b generates carry
            a=a^b;//a^b does the addition
            b=carry<<1;//we need to shift the carry left by 1 bit so that in next iteration it can be added to a
        }
        return a;
        
    }
}
