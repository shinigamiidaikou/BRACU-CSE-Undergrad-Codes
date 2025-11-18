import java.util.concurrent.ThreadLocalRandom;

public class InsertionTest {

	public static void main(String args[]) {
		System.out.println("Insertion Sort Times:");

		int[] arr;
		double startTime, elapsedTime;

		arr = randomArr(5000);
		startTime = System.nanoTime();
		insertionSort(arr);
		elapsedTime = System.nanoTime() - startTime;
		System.out.println("For 5000   Elements: " + (elapsedTime / 1000000) + " ms");
		
		arr = randomArr(50000);
		startTime = System.nanoTime();
		insertionSort(arr);
		elapsedTime = System.nanoTime() - startTime;
		System.out.println("For 50000  Elements: " + (elapsedTime / 1000000) + " ms");
		
		arr = randomArr(500000);
		startTime = System.nanoTime();
		insertionSort(arr);
		elapsedTime = System.nanoTime() - startTime;
		System.out.println("For 500000 Elements: " + (elapsedTime / 1000000) + " ms");
	}

	public static void printArr(int[] arr) {
		System.out.print("[" + arr[0]);
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

	/**
	 * Sort the specified array using insertion sort.
	 *
	 * @param arr the array containing the keys to sort
	 */
	public static void insertionSort(int[] arr) {
		for (int i = 1; i < arr.length; i++) {
			int key = arr[i];
			int j = i - 1;
			while (j >= 0 && arr[j] > key) {
				arr[j + 1] = arr[j];
				j--;
			}
			arr[j + 1] = key;
		}
	}
}