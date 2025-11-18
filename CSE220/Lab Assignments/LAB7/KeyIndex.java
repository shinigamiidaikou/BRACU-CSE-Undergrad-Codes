public class KeyIndex {
	private int[] k;
	private int keyDiff = 0;

	public KeyIndex(int[] a) {
		int min = a[0];
		int max = a[0];
		for (int i = 1; i < a.length; i++) {
			if (a[i] > max)
				max = a[i];
			if (a[i] < min)
				min = a[i];
		}
		if (min < 0)
			keyDiff = (-min);
		k = new int[max + keyDiff + 1];
		for (int i = 0; i < a.length; i++)
			k[a[i] + keyDiff]++;
	}

	/**
	 * A method to search for given value within the
	 * array and return true if found or false otherwise.
	 * 
	 * @param val -- the value provided
	 * @return true if found, else false
	 */
	public boolean search(int val) {
		try {
			if (k[val + keyDiff] > 0)
				return true;
		} catch (ArrayIndexOutOfBoundsException e) {
			return false;
		}
		return false;
	}

	/**
	 * A method to return the sorted form
	 * of the array which has been indexed
	 * 
	 * @return sorted indexed array
	 */
	public int[] sort() {
		int count = 0;
		for (int i = 0; i < k.length; i++) {
			count += k[i];
		}
		int[] newArr = new int[count];
		int i = 0;
		int j = 0;
		while (i < k.length) {
			if (k[i] > 0) {
				if (k[i] == 1) {
					newArr[j] = (i - keyDiff);
					j++;
				} else {
					count = k[i];
					while (count != 0) {
						newArr[j] = (i - keyDiff);
						j++;
						count--;
					}
				}
			}
			i++;
		}
		return newArr;
	}

}