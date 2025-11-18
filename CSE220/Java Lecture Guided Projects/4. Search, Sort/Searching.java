public class Searching {
	public static void main(String[] args) {
		Object[] arr = { 1, 2, 3, 4, 5, 6, 7, 8 };
		Object n = 8;
		System.out.println(seqSearch(arr, n));
		System.out.println(binSearch(arr, n));
	}

	/**
	 * Searches for the given key in the array of size elements.
	 * 
	 * @param arr the array with the keys
	 * @param key  the key to search for in the array
	 * @return the position of the key if found, or -1 otherwise.
	 */
	public static int seqSearch(Object[] arr, Object key) {
		for (int i = 0; i < arr.length; i++)
			if (key.equals(arr[i]))
				return i;
		return -1;
	}

	/**
	 * Searches for the given key in the array of size elements.
	 * Pre-condition: data must be sorted in non-decreasing order.
	 * 
	 * @param arr the array with the keys
	 * @param key  the key to search for in the array
	 * @return the position of the key if found, or -1 otherwise.
	 */
	public static int binSearch(Object[] arr, Object key) {
		int l = 0;
		int r = arr.length - 1;
		while (l <= r) {
			int mid = (l + r) / 2;
			if (key.equals(arr[mid]))
				return mid;
			else if (((Comparable) key).compareTo(arr[mid]) > 0)
				l = mid + 1;
			else
				r = mid - 1;
		}
		return -1;
	}
}
