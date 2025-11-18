public class linearArrayLab1 {
	public static void main(String[] args) {
		// Problem 1 driver code
		int[] source1 = { 10, 20, 30, 40, 50, 60 };
		shiftLeft(source1, 3);
		printArray(source1);
		// Problem 2 driver code
		int[] source2 = { 10, 20, 30, 40, 50, 60 };
		rotateLeft(source2, 3);
		printArray(source2);
		// Problem 3 driver code
		int[] source3 = { 10, 20, 30, 40, 50, 60 };
		shiftRight(source3, 3);
		printArray(source3);
		// Problem 4 driver code
		int[] source4 = { 10, 20, 30, 40, 50, 60 };
		rotateRight(source4, 3);
		printArray(source4);
		// Problem 5 driver code
		int[] source5 = { 10, 20, 30, 40, 50, 0, 0 };
		remove(source5, 5, 2);
		printArray(source5);
		// Problem 6 driver code
		int[] source6 = { 10, 2, 30, 2, 50, 2, 2, 0, 0 };
		removeAll(source6, 7, 2);
		printArray(source6);
		// Problem 7 driver code
		int[] source7 = { 10, 3, 1, 2, 10 };
		System.out.println(equalSplit(source7));
		// Problem 8 driver code
		int[] newSeriesArray = seriesArray(4);
		printArray(newSeriesArray);
		// Problem 9 driver code
		int[] source9 = { 1, 2, 2, 3, 4, 4, 4 };
		System.out.println(maxBunch(source9));
		// Problem 10 driver code
		int[] source10 = { 3, 4, 6, 3, 4, 7, 4, 6, 8, 6, 6 };
		System.out.println(repetition(source10));
	}

	// Array custom print method
	public static void printArray(int[] source) {
		System.out.print("[" + source[0] + ", ");
		for (int i = 1; i < source.length - 1; i++) {
			System.out.print(source[i] + ", ");
		}
		System.out.print(source[source.length - 1] + "]\n");
	}

	// Method 1:
	// Array left shift by K cells
	public static void shiftLeft(int array[], int k) {
		for (int j = 0; j < k; j++) {
			for (int i = 0; i < array.length - 1; i++) {
				array[i] = array[i + 1];
			}
			array[array.length - 1] = 0; // Now empty
		}
	}

	// Method 2:
	// Array left rotate by K cells
	public static void rotateLeft(int array[], int k) {
		for (int j = 0; j < k; j++) {
			int leftElement = array[0];
			for (int i = 0; i < array.length - 1; i++) {
				array[i] = array[i + 1];
			}
			array[array.length - 1] = leftElement;
		}
	}

	// Method 3:
	// Array right shift by K cells
	public static void shiftRight(int array[], int k) {
		for (int j = 0; j < k; j++) {
			for (int i = array.length - 1; i > 0; i--) {
				array[i] = array[i - 1];
			}
			array[0] = 0; // Now empty
		}
	}

	// Method 4:
	// Array right rotate by K cells
	public static void rotateRight(int array[], int k) {
		for (int j = 0; j < k; j++) {
			int rightElement = array[array.length - 1];
			for (int i = array.length - 1; i > 0; i--) {
				array[i] = array[i - 1];
			}
			array[0] = rightElement;
		}
	}

	// Method 5:
	// Remove a single element from an index
	public static void remove(int array[], int size, int idx) {
		if (idx < 0 || idx > size - 1) {
			System.out.println("Cannot Remove element!");
		} else {
			for (int i = idx; i < size - 1; i++) {
				array[i] = array[i + 1];
			}
			array[size - 1] = 0;
		}
	}

	// Method 6:
	// Remove all occurrences of a particular element
	public static void removeAll(int array[], int size, int element) {
		for (int i = 0; i < array.length; i++) {
			if (array[i] == element) {
				for (int j = i; j < size - 1; j++) {
					array[j] = array[j + 1];
				}
				array[size - 1] = 0;
				size--;
				i--;
			}
		}
	}

	// Method 7:
	// Array split
	public static boolean equalSplit(int array[]) {
		boolean equality_index_present = false;
		for (int i = 1; i < array.length; i++) {
			int total_left = 0, total_right = 0;
			for (int j = 0; j < i; j++) {
				total_left = total_left + array[j];
			}
			for (int j = i; j < array.length; j++) {
				total_right = total_right + array[j];
			}
			if (total_left == total_right) {
				equality_index_present = true;
				break;
			}
		}
		return equality_index_present;
	}

	// Method 8:
	// Array Series
	public static int[] seriesArray(int n) {
		int[] mainArray = new int[n * n];
		int[] secondaryArray = new int[n];
		// creating secondary array elements
		for (int i = 1; i < n + 1; i++) {
			secondaryArray[i - 1] = i;
		}
		int idx = mainArray.length - 1;
		for (int i = 0; i < n; i++) {
			// inserting elements from secondary array into main array
			for (int value : secondaryArray) {
				mainArray[idx] = value;
				idx--;
			}
			secondaryArray[n - i - 1] = 0;
		}
		return mainArray;
	}

	// Method 9:
	// Max bunch count
	public static int maxBunch(int[] array) {
		int maxCount = 0;
		if (array.length > 0) {
			if (array.length == 1) {
				maxCount = 1;
			} else {
				int element = array[0], count = 1;
				for (int i = 1; i < array.length; i++) {
					if (array[i] == element) {
						count++;
						if (i == array.length - 1 && maxCount < count) {
							maxCount = count;
						}
					} else {
						if (maxCount < count) {
							maxCount = count;
						}
						element = array[i];
						count = 1;
					}
				}
			}
		}
		return maxCount;
	}

	// Method 10:
	// Equal Repetition of any two elements
	public static boolean repetition(int[] array) {
		int[] cArray = new int[array.length];
		int[] nArray = new int[array.length];
		int idx = 0, currentIdx = 0;
		boolean found = false;
		nArray[0] = array[0];
		cArray[0] = 1;
		for (int i = 1; i < array.length; i++) {
			for (int j = 0; j < nArray.length; j++) {
				if (array[i] == nArray[j]) {
					idx = j;
					found = true;
					break;
				}
			}
			if (found == true) {
				cArray[idx]++;
				idx = 0;
				found = false;
			} else {
				currentIdx++;
				nArray[currentIdx] = array[i];
				cArray[currentIdx] = 1;
			}
		}
		boolean repetition = false;
		for (int i = 0; i < cArray.length - 1; i++) {
			for (int j = i + 1; j < cArray.length; j++) {
				if (cArray[i] == cArray[j] && cArray[i] > 1) {
					System.out.printf("%d %d\n", cArray[i], cArray[j]);
					System.out.printf("%d %d\n", i, j);
					repetition = true;
					break;
				}
			}
			if (repetition == true) {
				break;
			}
		}
		return repetition;
	}
}
