public class Recursion {
	public static void main(String[] args) throws Exception {
		// System.out.println(sumDigits(456)); // outputs: 15
		// System.out.println("==============");
		// System.out.println(bunnyEars2(0)); // outputs: 0
		// System.out.println(bunnyEars2(1)); // outputs: 2
		// System.out.println(bunnyEars2(2)); // outputs: 5
		// System.out.println(bunnyEars2(3)); // outputs: 7
		// System.out.println("==============");
		// System.out.println(count7(71717)); // outputs: 3
		// System.out.println("==============");
		// System.out.println(countX("xxhixx")); // outputs: 4
		// System.out.println(countX("xhixhix")); // outputs: 3
		// System.out.println(countX("hi")); // outputs: 0
		// System.out.println("==============");
		// System.out.println(changePi("xpix")); // outputs: "x3.14x"
		// System.out.println(changePi("pipi")); // outputs: "3.143.14"
		// System.out.println(changePi("pip")); // outputs: "3.14p"
		// System.out.println("==============");
		// int[] arr = { 1, 2, 3, 4 };
		// System.out.println(array11(arr, 0));
		// System.out.println("==============");
		// System.out.println(pairStar("hello")); // outputs: hel*lo
		// System.out.println(pairStar("xxyy")); // outputs: x*xy*y
		// System.out.println(pairStar("aaaa")); // outputs: a*a*a*a
		// System.out.println("==============");
		// System.out.println(countAbc("abc"));
		// System.out.println(countAbc("abcxxabc"));
		// System.out.println(countAbc("abaxxaba"));
		// System.out.println("==============");
		// System.out.println(countHi2("ahixhi"));
		// System.out.println(countHi2("ahibhi"));
		// System.out.println(countHi2("xhixhi"));
		// System.out.println("==============");
		// System.out.println(strCount("catcowcat", "cat"));
		// System.out.println(strCount("catcowcat", "cow"));
		// System.out.println(strCount("catcowcat", "dog"));
		// System.out.println("==============");
		// System.out.println(bunnyEars(0)); // outputs: 0
		// System.out.println(bunnyEars(1)); // outputs: 2
		// System.out.println(bunnyEars(2)); // outputs: 4
		// System.out.println("==============");
		// System.out.println(endX("xhixhix")); // outputs: rexx
		// System.out.println(count11("abc11x11x11"));
		// System.out.println(parenBit("xyz(abc)123"));
		int[] arr = { 2, 4, 8 };
		System.out.println(groupSum(0, arr, 11));
	}

	/*
	 * ======================
	 * PRACTICE SHEET SOLVES:
	 * ======================
	 */

	// Question-1:
	public static int sumDigits(int n) {
		if (n < 10) {
			return n;
		} else {
			return (n % 10) + sumDigits(n / 10);
		}
	}

	// Question-2:
	public static int bunnyEars2(int n) {
		if (n == 0)
			return 0;
		if (n == 1)
			return 2;
		else if (n % 2 == 0)
			return 3 + bunnyEars2(n - 1);
		else
			return 2 + bunnyEars2(n - 1);
	}

	// Question-3:
	public static int count7(int n) {
		if (n < 10) {
			if (n == 7)
				return 1;
			return 0;
		} else {
			if (n % 10 == 7)
				return 1 + count7(n / 10);
			return 0 + count7(n / 10);
		}
	}

	// Question-4:
	public static int countX(String string) {
		if (string.length() == 0)
			return 0;
		else {
			if (string.charAt(0) == 'x')
				return 1 + countX(string.substring(1));
			return 0 + countX(string.substring(1));
		}
	}

	// Question-5:
	public static String changePi(String string) {
		if (string.length() <= 1) {
			return string;
		} else {
			if (string.charAt(0) == 'p' && string.charAt(1) == 'i') {
				return "3.14" + changePi(string.substring(2));
			}
			return "" + string.charAt(0) + changePi(string.substring(1));
		}
	}

	// Question-6:
	public static int array11(int[] arr, int idx) {
		if (idx == arr.length - 1) {
			if (arr[idx] == 11)
				return 1;
			return 0;
		} else {
			if (arr[idx] == 11)
				return 1 + array11(arr, idx + 1);
			return 0 + array11(arr, idx + 1);
		}
	}

	// Question-7:
	public static String pairStar(String string) {
		if (string.length() <= 1) {
			return string;
		} else {
			if (string.charAt(0) == string.charAt(1)) {
				return "" + string.charAt(0) + "*" + pairStar(string.substring(1));
			}
			return "" + string.charAt(0) + pairStar(string.substring(1));
		}
	}

	// Question-8:
	public static int countAbc(String string) {
		if (string.length() <= 2)
			return 0;
		else {
			if (string.substring(0, 3).equals("abc") || string.substring(0, 3).equals("aba"))
				return 1 + countAbc(string.substring(3));
			return 0 + countAbc(string.substring(1));
		}
	}

	// Question-9
	public static int countHi2(String string) {
		if (string.length() <= 2) {
			if (string.equals("hi"))
				return 1;
			return 0;
		}
		if (string.length() <= 3) {
			if (string.equals("xhi"))
				return 0;
			return 0 + countHi2(string.substring(1));
		} else {
			if (string.substring(0, 3).equals("xhi"))
				return 0 + countHi2(string.substring(3));
			if (string.substring(0, 2).equals("hi"))
				return 1 + countHi2(string.substring(2));
			return 0 + countHi2(string.substring(1));
		}
	}

	// Question-10:
	public static int strCount(String main, String sub) {
		if (main.length() <= sub.length()) {
			if (main.equals(sub))
				return 1;
			return 0;
		} else {
			if (main.substring(0, sub.length()).equals(sub))
				return 1 + strCount(main.substring(sub.length()), sub);
			return 0 + strCount(main.substring(1), sub);
		}
	}

	// Question-11:
	public static int bunnyEars(int n) {
		if (n == 0)
			return 0;
		if (n == 1)
			return 2;
		else
			return 2 + bunnyEars(n - 1);
	}

	// Question-12:
	public static int triangle(int n) {
		if (n == 0)
			return 0;
		else
			return n + triangle(n - 1);
	}

	// Question-13:
	public static String noX(String string) {
		if (string.length() == 0)
			return "";
		else {
			if (string.charAt(0) == 'x')
				return noX(string.substring(1));
			return "" + string.charAt(0) + noX(string.substring(1));
		}
	}

	// Question-14
	public static boolean array220(int[] arr, int idx) {
		if (idx == arr.length - 1) {
			return false;
		} else {
			if (times10(arr, arr[idx], idx + 1))
				return true;
			return array220(arr, idx + 1);
		}
	}

	public static boolean times10(int[] arr, int val, int idx) {
		if (idx == arr.length - 1) {
			if (val * 10 == arr[idx])
				return true;
			return false;
		} else {
			if (val * 10 == arr[idx])
				return true;
			return times10(arr, val, idx + 1);
		}
	}

	// Question-15
	public static String endX(String string) {
		if (string.length() == 1) {
			if (string.charAt(0) == 'x')
				return "x";
			return string;
		} else {
			if (string.charAt(0) == 'x')
				return endX(string.substring(1)) + "x";
			return "" + string.charAt(0) + endX(string.substring(1));
		}
	}

	// Question-16:
	public static int count11(String string) {
		if (string.length() <= 1) {
			return 0;
		} else {
			if (string.substring(0, 2).equals("11"))
				return 1 + count11(string.substring(2));
			return 0 + count11(string.substring(1));
		}
	}

	// Question-17:
	public static String parenBit(String string) {
		if (string.length() != '(') {
			return parenBit(string.substring(1));
		}
		if (string.charAt(string.length() - 1) != ')')
			return parenBit(string.substring(0, string.length() - 1));
		return string;
	}

	public static boolean groupSum(int start, int[] array, int target) {
		if (start >= array.length) {
			return target == 0;
		} else {
			int remaining = target - array[start];
			if (groupSum(start + 1, array, remaining))
				return true;
			
			if (groupSum(start + 1, array, target))
				return true;
			
			return false;
		}
	}

	/*
	 * =============================
	 * Other Extra Basic Algorithms:
	 * =============================
	 */
	public static void printArrFwd(Object[] arr, int size) {
		if (size == 0) {
			System.out.println("[]");
			return;
		}
		if (size == 1) {
			try {
				Object temp = arr[1];
				arr[1] = temp;
				System.out.print("[" + arr[0] + ", ");
			} catch (ArrayIndexOutOfBoundsException e) {
				System.out.print("[" + arr[0] + "]\n");
			}
			return;
		}
		printArrFwd(arr, size - 1);
		if (size == arr.length)
			System.out.println(arr[size - 1] + "]");
		else
			System.out.print(arr[size - 1] + ", ");
	}

	public static void printArrBkwd(Object[] arr, int size) {
		if (size == 0)
			return;
		if (size == 1)
			System.out.println(arr[size - 1]);
		else
			System.out.print(arr[size - 1] + ", ");
		printArrBkwd(arr, size - 1);
	}

	/**
	 * Recursive function to search index for
	 * desired object in an Object array.
	 * 
	 * @param arr  -- reference to given array
	 * @param size -- number of elements
	 * @param key  -- desired object to find
	 * 
	 * @return index of searched key
	 */
	public static int search(Object[] arr, int size, Object key) {
		if (size - 1 < 0)
			return -1;
		if (key == arr[size - 1])
			return size - 1;
		size--;
		return search(arr, size, key);
	}

	/**
	 * Recursive function to find maximum value stored in an integer array.
	 * 
	 * @param arr  -- reference to given array
	 * @param size -- number of elements
	 * @return Max value of array.
	 * @throws Exception Empty array! Max value unavailable.
	 */
	public static Object findMax(Object[] arr, int size) throws Exception {
		if (size == 0) {
			throw new Exception("Empty array! Max value unavailable.");
		}
		// Base Case:
		if (size == 1)
			return arr[0];
		// Recursive Call:
		else {
			Object lastMax = findMax(arr, size - 1);
			if ((int) arr[size - 1] > (int) lastMax)
				return arr[size - 1];
			return lastMax;
		}
	}

	/**
	 * Recursive function to find Nth fibpnacchi number.
	 * 
	 * @param n -- the n-th term to print upto
	 * @return 'N' th fibonacchi value
	 */
	public static int RFibonacchi(int n) {
		if (n < 0) {
			System.out.println("Invalid term!");
			return -1;
		}
		if (n < 2)
			return n;
		else {
			return RFibonacchi(n - 1) + RFibonacchi(n - 2);
		}
	}

	public static int Fibonacchi(int n) {
		if (n < 0) {
			System.out.println("Invalid term!");
			return -1;
		}
		// Create and initialize the table.
		int[] F = new int[n + 1];
		for (int i = 0; i <= n; i++)
			F[i] = -1; // No solution saved in F[i] yet.
		// Now we can call M-Fib with this extra parameter "F".
		return Mfibonacchi(n, F);
	}

	private static int Mfibonacchi(int n, int[] F) {
		if (F[n] < 2)
			F[n] = n;
		else {
			if (F[n] != -1)
				F[n] = Mfibonacchi(n - 1, F) + Mfibonacchi(n - 2, F);
		}
		return F[n];
	}

	/**
	 * Recursive function to find n! (factorial_n)
	 * 
	 * @param N -- the number to calculate factorial of
	 * @return 1 if N = 1, else N * factorial(N - 1)
	 */
	public static int factorial(int N) {
		if (N == 1)
			return 1;
		return N * factorial(N - 1);
	}

	/**
	 * @param x -- Base value
	 * @param n -- Power
	 * @return value of x^n
	 */
	public static int power(int x, int n) {
		if (n == 1)
			return x;
		return x * power(x, n - 1);
	}

}