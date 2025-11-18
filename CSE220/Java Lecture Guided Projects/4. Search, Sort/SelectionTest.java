import java.util.concurrent.ThreadLocalRandom;

public class SelectionTest {

	public static void main(String args[]) {
		System.out.println("Selection Sort Times:");
		
		int[] arr;
		double startTime, elapsedTime;
		
		arr = randomArr(5000);
		startTime = System.nanoTime();
		selectSort(arr);
		elapsedTime = System.nanoTime() - startTime;
		printArr(arr);
		System.out.println("For 5000   Elements: " + (elapsedTime / 1000000) + " ms");

		arr = randomArr(50000);
		startTime = System.nanoTime();
		selectSort(arr);
		elapsedTime = System.nanoTime() - startTime;
		printArr(arr);
		System.out.println("For 50000  Elements: " + (elapsedTime / 1000000) + " ms");

		arr = randomArr(500000);
		startTime = System.nanoTime();
		selectSort(arr);
		elapsedTime = System.nanoTime() - startTime;
		System.out.println("For 500000 Elements: " + (elapsedTime / 1000000) + " ms");
	}

	public static void printArr(int[] arr) {
		System.out.print("["+arr[0]);
		for (int i = 1; i < arr.length; i++)
			System.out.print(", " + arr[i]);
		System.out.print("]\n");
	}

	public static int[] randomArr(int Length) {
		int[] arr = new int[Length];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = ThreadLocalRandom.current().nextInt(1, Length + 1);
		}
		return arr;
	}

	public static void selectSort(int[] arr) {
		int min_idx, swap;
		for (int i = 0; i < arr.length - 1; i++) {
			min_idx = i;
			for (int j = i + 1; j < arr.length; j++) {
				if (arr[min_idx] > arr[j])
					min_idx = j;
			}
			swap = arr[i];
			arr[i] = arr[min_idx];
			arr[min_idx] = swap;
		}
	}

}
