public class Lab6_3 {
	public static void main(String[] args) {
		Lab6_3 obj1 = new Lab6_3();
		int x = obj1.hocBuilder(3);
		System.out.println("Num of Cards Required: "+ x);
	}

	public int hocBuilder (int height) { 
		if (height == 0) {
			return 0;
		} if (height == 1) {
			return 8;
		} else {
			return 5 + hocBuilder(height - 1);
		}
	} 
}