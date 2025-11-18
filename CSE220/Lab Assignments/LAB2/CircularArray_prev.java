public class CircularArray {

	private int start;
	private int size;
	private Object[] cir;

	/*
	 * if Object [] lin = { 10, 20, 30, 40, null }
	 * then, CircularArray(lin, 2, 4) will generate
	 * Object [] cir = { 40, null, 10, 20, 30 }
	 */

	public CircularArray(Object[] lin, int st, int sz) {
		start = st;
		size = sz;
		cir = new Object[lin.length];
		int idx = start;
		for (int i = 0; i < size; i++) {
			cir[idx] = lin[i];
			idx = (idx + 1) % lin.length;
		}
	}

	// Prints from index --> 0 to cir.length-1
	public void printFullLinear() {
		for (int i = 0; i < cir.length - 1; i++) {
			System.out.print(cir[i] + ", ");
		}
		System.out.println(cir[cir.length - 1]);
	}

	// Starts Printing from index start. Prints a total of size elements
	public void printForward() {
		int idx = start;
		for (int i = 0; i < size - 1; i++) {
			System.out.print(cir[idx] + ", ");
			idx = (idx + 1) % cir.length;
		}
		System.out.println(cir[idx]);
	}

	public void printBackward() {
		int idx = (start + size - 1) % cir.length;
		for (int i = 0; i < size - 1; i++) {
			System.out.print(cir[idx] + ", ");
			idx--;
			if (idx < 0) {
				idx = cir.length - 1;
			}
		}
		System.out.println(cir[idx]);
	}

	// With no null cells
	public void linearize() {
		Object[] lin = new Object[size];
		int idx = start;
		for (int i = 0; i < size; i++) {
			lin[i] = cir[idx];
			idx = (idx + 1) % cir.length;
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
		int fwd_idx = start;
		int bckwd_idx = (start + size - 1) % cir.length;
		boolean palindrome = true;
		for (int i = 0; i < size / 2; i++) {
			if (cir[fwd_idx] != cir[bckwd_idx]){
				palindrome = false;
				System.out.println("This array is NOT a palindrome.");
				break;
			}
			fwd_idx = (fwd_idx + 1) % cir.length;
			bckwd_idx--;
			if (bckwd_idx < 0) {
				bckwd_idx = cir.length - 1;
			}
		}
		if (palindrome == true) {
			System.out.println("This array is a palindrome.");
		}
	}

	// This method will sort the values by keeping the start unchanged
	public void sort() {
		int main_idx = start;
		for (int i = 0; i < size - 1; i++) {
			int sub_idx = (main_idx + 1) % cir.length;
			for (int j = i + 1; j < size; j++) {
				if ((int) cir[main_idx] > (int) cir[sub_idx]) {
					Object temp = cir[main_idx];
					cir[main_idx] = cir[sub_idx];
					cir[sub_idx] = temp;
				}
				sub_idx = (sub_idx + 1) % cir.length;
			}
			main_idx = (main_idx + 1) % cir.length;
		}
	}

	// This method will check the given array across the base array and if they
	// are equivalent in terms of values return true, or else return false
	public boolean equivalent(CircularArray k) {
		if (size != k.size) {
			return false;
		}
		int idx1 = start, idx2 = k.start;
		for (int i = 0; i < size; i++) {
			if ((int) cir[idx1] != (int) k.cir[idx2]) {
				return false;
			}
			idx1 = (idx1 + 1) % cir.length;
			idx2 = (idx2 + 1) % k.cir.length;
		}
		return true;
	}

	// This method takes another circular array and returns a linear array
	// containing the common elements between the two circular arrays.
	public int[] intersection(CircularArray c2) {
		int[] lin;
		if (size < c2.size) {
			lin = new int[size];
		} else {
			lin = new int[c2.size];
		}
		int count = 0;
		int idx1 = start;
		for (int i = 0; i < size; i++) {
			int idx2 = c2.start;
			for (int j = 0; j < c2.size; j++) {
				if ((int) cir[idx1] == (int) c2.cir[idx2]) {
					lin[count] = (int) cir[idx1];
					count++;
				}
				idx2 = (idx2 + 1) % c2.cir.length;
			}
			idx1 = (idx1 + 1) % cir.length;
		}
		int[] newLin = new int[count];
		for (int i = 0; i < count; i++) {
			newLin[i] = lin[i];
		}
		return newLin;
	}
}