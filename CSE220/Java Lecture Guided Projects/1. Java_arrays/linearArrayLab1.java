public class linearArrayLab1 {
	public static void main(String[] args){
		int []arr = {10, 20, 30, 40, 50, 60};
		//int[] arr = new int[8];
		//int count = 10, s = 6;
		//for(int i=0; i<s; i++){
		//	arr[i] = count;
		//	count += 10;
		//}
		//print(arr);
		//System.out.println("Changed Array:");
		kShiftLeft(arr, 2);
		print(arr);
	}
	// array element print method
	public static void print(int[] source){
		for(int value: source){
			System.out.println(value);
		}
	}
	// array left shift by K cells method
	public static void kShiftLeft(int array[], int k){
		for (int j = 0; j < k; j++){
			for (int i = 0; i < array.length - 1; i++){
				array[i] = array[i + 1];
			}
			array[array.length - 1] = 0; // Now empty
		}
	}
	// array left rotate by K cells method
	public static void kRotateLeft(int array[], int k){
		for (int j = 0; j < k; j++){
			int leftElement = array[0];
			for (int i = 0; i < array.length - 1; i++){
				array[i] = array[i+1];
			}
			array[array.length - 1] = leftElement;
		}
	}
	// array right shift by K cells method
	public static void kShiftRight(int array[], int k){
		for (int j = 0; j < k; j++){
			for (int i = array.length - 1; i > 0; i--){
				array[i] = array[i - 1];
			}
			array[0] = 0; // Now empty
		}
	}
	// array right rotate by K cells method
	public static void kRotateRight(int array[], int k){
		for (int j = 0; j < k; j++){
			int rightElement = array[array.length - 1];
			for (int i = array.length - 1; i > 0; i--){
				array[i] = array[i - 1];
			}
			array[0] = rightElement;
		}
	}
	// array remove single element from given index method
	public static void remove(int array[], int size, int idx){
		if (idx < 0 || idx > size - 1){
			System.out.println("Cannot Remove element!");
		} else{
			for (int i = idx; i < size - 1; i++){
				array[i] = array[i+1];
			}
			array[size-1] = 0;
		}
	}
	// array remove all same elements method
	public static void removeAll(int array[], int size, int element){
		for (int i = 0; i < array.length; i++){
			if (array[i] == element){
				for (int j = i; j < size - 1; j++){
					array[j] = array[j+1];
				}
				array[size-1] = 0;
				size--;
				i--;
			}
		}
	}
	// array split method
	public static void equalSplit(int array[]){
		boolean equality_index_present = false;
		for (int i = 1; i < array.length; i++){
			int total_left = 0, total_right = 0;
			for (int j = 0; j < i; j++){
				total_left = total_left + array[j];
			}
			for (int j = i; j < array.length; j++){
				total_right = total_right + array[j];
			}
			if (total_left == total_right){
				equality_index_present = true;
				break;
			}
		}
		System.out.println(equality_index_present);
	}
}
