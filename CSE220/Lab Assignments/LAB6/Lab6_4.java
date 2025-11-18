public class Lab6_4 {
	public static void main(String[] args) {
		int n = 7;
		System.out.println("------------------");
		System.out.println("## 1st Triangle:");
		System.out.println("------------------");
		rightAngleLeftTriangle(n);
		System.out.println("------------------");
		System.out.println("## 2nd Triangle:");
		System.out.println("------------------");
		rightAngleRightTriangle(n);
	}

	public static void rightAngleLeftTriangle(int n) {
		if (n == 1) {
			System.out.print(intRow(1) + "\n");
		} else {
			rightAngleLeftTriangle(n - 1);
			System.out.print(intRow(n) + "\n");
		}
	}

	public static void rightAngleRightTriangle(int n) {
		rightAngleRightTriangle(n, 0);
	}

	public static void rightAngleRightTriangle(int n, int s) {
		if (n == 1) {
			System.out.print(" ".repeat(s * 2) + intRow(1) + "\n");
		} else {
			rightAngleRightTriangle(n - 1, s + 1);
			System.out.print(" ".repeat(s * 2) + intRow(n) + "\n");
		}
	}

	public static String intRow(int n) {
		if (n == 1) {
			return "1";
		} else {
			return intRow(n - 1) + " " + n;
		}
	}

}
