public class Question1 {

	public static void main(String[] args) {
		Question1 q1 = new Question1();
		
		int[] arr1 = { 7, 1, 5, 15, 52, 26, 2, 3, 0, 0 };
		int[] npcArr = q1.nonPrimeCircular(arr1, 8);
		q1.fullLinearPrint(npcArr);
		
		int[] arr2 = { 7, 1, 5, 2, 3, 0, 0 };
		npcArr = q1.nonPrimeCircular(arr2, 5);
		q1.fullLinearPrint(npcArr);

	}

	public void fullLinearPrint(int[] arr) {
		if (arr.length == 0) {
			System.out.println("[]");
		} else if (arr.length == 1) {
			System.out.print("[" + arr[0] + "]");
		} else {
			System.out.print("[" + arr[0] + ", ");
			for (int i = 1; i < arr.length - 1; i++) {
				System.out.print(arr[i] + ", ");
			}
			System.out.print(arr[arr.length - 1] + "]\n");
		}
	}

	public int[] nonPrimeCircular(int[] arr, int size) {
		int[] nonPrime = new int[arr.length];
		int nonPrimeCount = 0;
		for (int i = 2; i < size - 1; i++) {
			boolean divFound = false;
			int temp = arr[i] - 1;
			while (temp > 1) {
				if (arr[i] % temp == 0) {
					divFound = true;
					break;
				}
				temp--;
			}
			if (divFound == true) {
				nonPrime[nonPrimeCount] = arr[i];
				nonPrimeCount++;
			}
		}
		if (nonPrimeCount == 0) {
			System.out.println("All are prime");
			return new int[0];
		} else {
			int[] cir = new int[nonPrimeCount];
			int idx = cir.length - 1;
			for (int i = nonPrimeCount - 1; i >= 0; i--) {
				cir[idx] = nonPrime[i];
				idx = (idx + 1) % cir.length;
			}
			return cir;
		}
	}
}