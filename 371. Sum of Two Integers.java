class Solution {
    public int getSum(int a, int b) {

        int ans = a ^ b;
        int carry = (a & b) << 1;

        while (carry != 0){
            int newAns = ans ^ carry;
            carry = (ans & carry) << 1;
            ans = newAns;
        }
        
        return ans;
    }
}
