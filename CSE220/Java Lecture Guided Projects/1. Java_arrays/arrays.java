public class arrays {
	public static void main(String[] args){
		int []arr = { 10, 20, 30, 40, 50, 60 };
		//int[] arr = new int[10];
		//int count = 10, s = 7;
		//for(int i=0; i<s; i++){
		//	arr[i] = count;
		//	count += 10;
		//}
		printArray(arr);
	}
	
	// Array one/one element print method
	public static void print(int[] source){
		for(int value: source){
			System.out.println(value);
		}
	}
	// Full array single line print method
	public static void printArray(int[] source) {
		System.out.print("[" + source[0] + ", ");
		for (int i = 1; i < source.length - 1; i++) {
			System.out.print(source[i] + ", ");
		}
		System.out.print(source[source.length - 1] + "]\n");
	}
	
	// array manual copy method
	public static Object[] copyArray(Object[] source){
		Object[] new_copy = new Object[source.length];
		for (int i = 0; i < source.length; i++){
			new_copy[i] = source[i];
		}
		return new_copy;
	}
	// array copy method (java.util package)
	//public static Object[] copyArray(Object[] source){
	//	Object[] new_copy = java.util.Arrays.copyOf(source, source.length);
	//	return new_copy;
	//}

	// array-resize (Increase size) method
	public static Object[] resize(Object[] oldArray, int newCapacity){
		Object[] newArray = new Object[newCapacity];
		for (int i = 0; i < oldArray.length; i++)
		newArray[i] = oldArray[i];
		return newArray;
	}
	
	// array-reverse method (In place method)
	public static void reverse(Object[] source){
		int i = 0; // forward index into left half
		int j = source.length - 1; // backward index into right half
		while (i < j) {
		// Exchange array[i] with array[j]
			Object tmp = source[i];
			source[i] = source[j];
			source[j] = tmp;
			i++;
			j--;
		}
	}
	
	// array left shift method
	public static void shiftLeft(Object array[]){
		for (int i = 0; i < array.length -1; i++){
			array[i] = array[i + 1];
		}
		array[array.length - 1] = null; // Now empty
	}
	// array right shift method
	public static void shiftRight(Object array[]) {
		for (int i = array.length - 1; i > 0; i--){
			array[i] = array[i - 1];
		}
		array[0] = null; // Now empty.
	}
	
	// array rotate left method
	public static void rotateLeft(Object array[]) {
		Object firstElement = array[0];
		for (int i = 1; i < array.length; i++){
			array[i - 1] = array[i];
		}
		array[array.length - 1] = firstElement;
	}
	// array rotate right method
	public static void rotateRight(Object array[]) {
		Object lastElement = array[array.length - 1];
		for (int i = array.length - 1; i > 0; i--){
			array[i] = array[i - 1];
		}
		array[0] = lastElement;
	}
}
