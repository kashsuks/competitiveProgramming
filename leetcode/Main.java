import java.util.*;

public class Solution {
    public int someFunction(int[] nums) {
        // Your code here
        return 0; // Adjust return type based on the problem
    }
    
    public static void main(String[] args) {
        // Test cases can be added here
        Solution solution = new Solution();
        
        // Example test case
        int[] nums = {1, 2, 3};
        int result = solution.someFunction(nums);
        System.out.println(result);
    }
}
//Start of template by Kashyap Sukshavasi
class Utils {
    public static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static long lcm(long a, long b) {
        return (a / gcd(a, b)) * b;
    }

    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static long modExp(long base, long exp, long mod) {
        long result = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) result = (result * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    }
}
//End of template by Kashyap Sukshavasi
