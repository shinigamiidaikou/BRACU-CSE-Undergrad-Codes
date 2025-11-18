import java.util.concurrent.ThreadLocalRandom;

public class AarraySearchSort {
	public static void main(String[] args) {
		int[] arr1 = randomArr(8, 1, 14);
		printArr(arr1);
		selectionSort(arr1, 0);
		printArr(arr1);
	}

	public static void printArr(int[] arr) {
		System.out.print("[");
		if (arr.length != 0)
			System.out.print(arr[0]);
		for (int i = 1; i < arr.length; i++)
			System.out.print(", "+arr[i]);
		System.out.print("]\n");
	}

	public static int[] randomArr(int length, int startInc, int endExc) {
		int[] arr = new int[length];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = ThreadLocalRandom.current().nextInt(startInc, endExc + 1);
		}
		return arr;
	}

	public static void selectionSort(int[] arr, int idx) {
		if (idx == arr.length - 1) {
			return;
		} else {
			int j = minIndex(arr, idx);
			if (j != idx) {
				int swap = arr[idx];
				arr[idx] = arr[j];
				arr[j] = swap;
			}
			selectionSort(arr, idx + 1);
		}
	}

	public static int minIndex(int[] arr, int idx) {
		if (idx == arr.length - 1) {
			return idx;
		} else {
			int j = minIndex(arr, idx + 1);
			if (arr[idx] > arr[j]) {
				return j;
			} else {
				return idx;
			}
		}
	}
}