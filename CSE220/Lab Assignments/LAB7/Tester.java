public class Tester {
	public static void main(String[] args) {
		System.out.println("==================================");
		System.out.println("Test- 1:");
		System.out.println("----------------------------------");
		int[] a = { 2, 2, 4, 6, 1, 6, 6, 0, 5, -1, -1, -7, -2, -3 };
		printArr(a);
		KeyIndex aIndex = new KeyIndex(a);
		System.out.println(aIndex.search(7));
		int[] newArr = aIndex.sort();
		printArr(newArr);
		System.out.println("==================================");
		System.out.println("Test- 2:");
		System.out.println("----------------------------------");
		int[] b = { 5, 3 ,7 ,1 , 4, 4, 2,7,3};
		printArr(b);
		KeyIndex bIndex = new KeyIndex(b);
		System.out.println(bIndex.search(2));
		newArr = bIndex.sort();
		printArr(newArr);
		System.out.println("==================================");
	}

	public static void printArr(int[] arr) {
		System.out.print("[" + arr[0]);
		for (int i = 1; i < arr.length; i++) {
			System.out.print(", " + arr[i]);
		}
		System.out.print("]\n");
	}
}