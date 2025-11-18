import java.util.Scanner;

public class Lab6_1 {
	public static void main(String[] args) {
		int n = 0;
		System.out.print("n = ");
		try (Scanner newScan = new Scanner(System.in)) {
			n = newScan.nextInt();
		}
		System.out.println("Factorial of n: " + factorial(n));
		System.out.println("nth Fibonacchi: " + fibonacchi(n));
		int[] intArr = { 1, 3, 5, 7, 9, 11 };
		printForward(intArr, intArr.length);
		int base = 3;
		n = 3;
		System.out.println(base + "^" + n + " = " + powerN(base, n));
	}

	public static int factorial(int n) {
		if (n < 0)
			throw new ArithmeticException("n < 0");
		if (n == 0)
			return 1;
		else
			return (n * factorial(n - 1));
	}

	public static int fibonacchi(int n) {
		if (n == 1) {
			return 0;
		}
		if (n == 2) {
			return 1;
		} else {
			return fibonacchi(n - 1) + fibonacchi(n - 2);
		}
	}

	public static void printForward(int[] intArr, int n) {
		if (n == 0) {
			return;
		}
		if (n == 1) {
			System.out.print(intArr[0]);
		} else {
			printForward(intArr, n - 1);
			System.out.print(", " + intArr[n - 1]);
		}
		if (n == intArr.length) {
			System.out.print("\n");
		}
	}

	private static int powerN(int b, int n) {
		if (n == 0) {
			return 1;
		} else {
			return b * powerN(b, n - 1);
		}
	}

}
