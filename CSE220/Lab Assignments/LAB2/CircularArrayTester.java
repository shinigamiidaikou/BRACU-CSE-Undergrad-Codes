public class CircularArrayTester {
	public static void main(String[] args) {

		Object[] linear = { 10, 20, 30, 40, null };

		System.out.println("\n///// TEST 01 /////");
		CircularArray c = new CircularArray(linear, 2, 4);
		c.printFullLinear(); // This Should Print: 40, null, 10, 20, 30.
		c.printForward(); // This Should Print: 10, 20, 30, 40.
		c.printBackward(); // This Should Print: 40, 30, 20, 10.

		System.out.println("\n///// TEST 02 /////");
		c.linearize();
		c.printFullLinear(); // This Should Print: 10, 20, 30, 40.

		System.out.println("\n///// TEST 03 /////");
		Object[] linear2 = { 10, 20, 30, 40, 50 };
		CircularArray c2 = new CircularArray(linear2, 2, 5);
		c2.printFullLinear(); // This Should Print: 40, 50, 10, 20, 30.
		c2.resizeStartUnchanged(8); // parameter--> new Capacity
		c2.printFullLinear(); // This Should Print: null, null, 10, 20, 30, 40, 50, null.

		System.out.println("\n///// TEST 04 /////");
		Object[] linear3 = { 10, 20, 30, 20, 10, null, null };
		CircularArray c3 = new CircularArray(linear3, 3, 5);
		c3.printForward(); // This Should Print: 10, 20, 30, 20, 10.
		c3.palindromeCheck(); // This Should Print: This array is a palindrome.

		System.out.println("\n///// TEST 5 /////");
		Object[] linear4 = { 10, 20, 30, 20, null, null, null };
		CircularArray c4 = new CircularArray(linear4, 3, 4);
		c4.printForward(); // This Should Print: 10, 20, 30, 20.
		c4.palindromeCheck(); // This Should Print: This array is NOT a palindrome.

		System.out.println("\n///// TEST 6 /////");
		Object[] linear5 = { 10, 20, -30, 20, 50, 30, null };
		CircularArray c5 = new CircularArray(linear5, 5, 6);
		c5.printForward(); // This Should Print: 10, 20, -30, 20, 50, 30.
		c5.sort();
		c5.printForward(); // This Should Print: -30, 10, 20, 20, 30, 50.

		System.out.println("\n///// TEST 7 /////");
		Object[] linear6 = { 10, 20, -30, 20, 50, 30, null };
		CircularArray c6 = new CircularArray(linear6, 2, 6);
		CircularArray c7 = new CircularArray(linear6, 5, 6);
		c6.printForward(); // This Should Print: 10, 20, -30, 20, 50, 30.
		c7.printForward(); // This Should Print: 10, 20, -30, 20, 50, 30.
		System.out.println(c6.equivalent(c7)); // This Should Print: true

		System.out.println("\n///// TEST 8 /////");
		Object[] linear7 = { 10, 20, -30, 20, 50, 30, null, null, null };
		c7 = new CircularArray(linear7, 8, 6);
		c6.printForward(); // This Should Print: 10, 20, -30, 20, 50, 30.
		c7.printForward(); // This Should Print: 10, 20, -30, 20, 50, 30.
		System.out.println(c6.equivalent(c7)); // This Should Print: true

		System.out.println("\n///// TEST 9 /////");
		Object[] linear8 = { 10, 20, 30, 40, 50, 60, null, null, null };
		CircularArray c8 = new CircularArray(linear8, 8, 6);
		c6.printForward(); // This Should Print: 10, 20, -30, 20, 50, 30.
		c8.printForward(); // This Should Print: 10, 20, 30, 40, 50, 60
		System.out.println(c6.equivalent(c8)); // This Should Print: false

		System.out.println("\n///// TEST 10 /////");
		Object[] linear9 = { 10, 20, 30, 40, 50, null, null, null };
		CircularArray c9 = new CircularArray(linear9, 5, 5);
		c9.printFullLinear(); // This should print: 40, 50, null, null, null, 10, 20, 30
		Object[] linear10={5,40,15,25,10,20,5,null,null,null,null,null};
		CircularArray c10 = new CircularArray(linear10, 8, 7);
		c10.printFullLinear(); // This should print: 10, 20, 5, null, null, null, null, null, 5, 40, 15, 25
		int[] output = c9.intersection(c10);
		for (int i = 0; i < output.length; ++i) {
			System.out.print(output[i] + " "); // This should print: 10 20 40
		}
	}
}