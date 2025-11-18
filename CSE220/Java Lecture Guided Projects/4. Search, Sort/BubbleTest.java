import java.util.concurrent.ThreadLocalRandom;

public class BubbleTest {

	public static void main(String args[]) {
		System.out.println("Bubble Sort Times:");
		
		int[] arr;
		double startTime, elapsedTime;
		
		arr = randomArr(5000);
		startTime = System.nanoTime();
		bubbleSort(arr);
		elapsedTime = System.nanoTime() - startTime;
		System.out.println("For 5000   Elements: " + (elapsedTime / 1000000) + " ms");

		arr = randomArr(50000);
		startTime = System.nanoTime();
		bubbleSort(arr);
		elapsedTime = System.nanoTime() - startTime;
		System.out.println("For 50000  Elements: " + (elapsedTime / 1000000) + " ms");
		
		arr = randomArr(500000);
		startTime = System.nanoTime();
		bubbleSort(arr);
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

	private static void bubbleSort(int[] arr) {
		int swap;
		for (int i = 0; i < arr.length - 1; i++) {
			for (int j = 0; j < arr.length - i - 1; j++) {
				if (arr[j] > arr[j+1]) {
					swap = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = swap;
				}
			}
		}
	}

}