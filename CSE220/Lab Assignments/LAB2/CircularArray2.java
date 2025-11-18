public class CircularArray {

	private int start;
	private int size;
	private Object[] cir;

	/*
	 * if Object [] lin = {10, 20, 30, 40, null}
	 * then, CircularArray(lin, 2, 4) will generate
	 * Object [] cir = {40, null, 10, 20, 30}
	 */
	 
	public CircularArray(Object[] lin, int st, int sz) {
		start = st;
		size = sz;
		cir = new Object[lin.length];
		for (int i = 0; i < size; i++) {
			cir[(i + start) % cir.length] = lin[i];
		}
	}

	// Prints from index --> 0 to cir.length-1
	public void printFullLinear() {
		for (int i = 0; i < cir.length; i++) {
			if (i == cir.length - 1) {
				System.out.println(cir[i]);
			} else {
				System.out.print(cir[i] + ", ");
			}
		}
	}

	// Starts Printing from index start. Prints a total of size elements
	public void printForward() {
		//int idx = start;
		for (int i = 0; i < size; i++) {
			if (i == size - 1) {
				//System.out.println(cir[idx]);
				System.out.println(cir[(i + start) % cir.length]);
			} else {
				//System.out.print(cir[idx] + ", ");
				System.out.print(cir[(i + start) % cir.length] + ", ");
			}
			//idx = (idx + 1) % cir.length;
		}
	}

	public void printBackward() {
		int idx = (start + size - 1) % cir.length;
		for (int i = 0; i < size; i++) {
			if (i == size - 1) {
				System.out.println(cir[idx]);
			} else {
				System.out.print(cir[idx] + ", ");
			}
			idx--;
			if (idx < 0) {
				idx = cir.length - 1;
			}
		}
	}

	// With no null cells
	public void linearize() {
		Object[] lin = new Object[size];
		//int idx = start;
		for (int i = 0; i < size; i++) {
			//lin[i] = cir[idx];
			lin[i] = cir[(i + start) % cir.length];
			//idx = (idx + 1) % cir.length;
		}
		cir = lin;
	}

	// Do not change the Start index
	public void resizeStartUnchanged(int newcapacity) {
		Object[] newCir = new Object[newcapacity];
		int idx = start;
		int newidx = start;
		for (int i = 0; i < size; i++) {
			newCir[newidx] = cir[idx];
			idx = (idx + 1) % cir.length;
			newidx = (newidx + 1) % newCir.length;
		}
		cir = newCir;
	}

	// This method will check whether the array is palindrome or not
	public void palindromeCheck() {
		int f_i = start;
		int b_i = (start + size - 1) % cir.length;
		boolean palindrome = true;
		for (int i = 0; i < size / 2; i++) {
			if ((int) cir[f_i] != (int) cir[b_i]) {
				palindrome = false;
				System.out.println("This array is NOT a palindrome.");
				break;
			}
			f_i = (f_i + 1) % cir.length;
			b_i--;
			if (b_i < 0) {
				b_i = cir.length - 1;
			}
		}
		if (palindrome == true) {
			System.out.println("This array is a palindrome.");
		}
	}

	// This method will sort the values by keeping the start unchanged
	public void sort() {
		for (int i = 0; i < size - 1; i++) {
			int idx1 = start;
			int idx2 = (idx1 + 1) % cir.length;
			for (int j = 0; j < size - i - 1; j++) {
				if ((int) cir[idx1] > (int) cir[idx2]) {
					Object temp = (int) cir[idx2];
					cir[idx2] = cir[idx1];
					cir[idx1] = temp;
				}
				idx1 = (idx1 + 1) % cir.length;
				idx2 = (idx2 + 1) % cir.length;
			}
		}
	}

	// This method will check the given array across the base array and if they are
	// equivalent interms of values return true, or else return false
	public boolean equivalent(CircularArray k) {
		if (size != k.size) {
			return false;
		}
		int idx1 = start;
		int idx2 = k.start;
		for (int i = 0; i < size; i++) {
			if ((int) cir[idx1] != (int) k.cir[idx2]) {
				return false;
			}
			idx1 = (idx1 + 1) % cir.length;
			idx2 = (idx2 + 1) % k.cir.length;
		}
		return true;
	}

	// This the method take another circular array and returns a linear array
	// containing the common elements between the two circular arrays.
	public int[] intersection(CircularArray c2) {
		int[] lin;
		if (size < c2.size) {
			lin = new int[size];
		} else {
			lin = new int[c2.size];
		}
		int idx1 = start;
		int newsize = 0;
		for (int i = 0; i < size; i++) {
			int idx2 = c2.start;
			for (int j = 0; j < c2.size; j++) {
				if ((int) cir[idx1] == (int) c2.cir[idx2]) {
					lin[newsize] = (int) cir[idx1];
					newsize++;
				}
				idx2 = (idx2 + 1) % c2.cir.length;
			}
			idx1 = (idx1 + 1) % cir.length;
		}
		int[] final_arr = new int[newsize];
		for (int i = 0; i < newsize; i++) {
			final_arr[i] = lin[i];
		}
		return final_arr;
	}
}