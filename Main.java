//Start of Kashyap Sukshavasi template for CP
import java.io.*;
import java.util.*;

public class Main {

    static class FastIO {
        BufferedReader br;
        StringTokenizer st;

        public FastIO() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    static class Utils {
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
//End of Kashyap Sukshavasi template for CP
    public static void main(String[] args) {
        FastIO io = new FastIO();
        PrintWriter out = new PrintWriter(System.out);

        int t = io.nextInt();
        while (t-- > 0) {
            int a = io.nextInt();
            int b = io.nextInt();
            out.println(a + b);
        }

        out.flush();
    }
}
