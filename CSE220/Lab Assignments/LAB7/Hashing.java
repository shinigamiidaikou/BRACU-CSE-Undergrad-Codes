public class Hashing {
	public static void main(String[] args) {
		System.out.println("----------------------------------------");
		String[] arr = { "ST1E89B8A32", "HSDGF345E", "DEE34ERE" };
		printArr(arr);
		String[] hashedArr = hashTable(arr);
		System.out.println("Hash Table:");
		printArr(hashedArr);
		System.out.println("----------------------------------------");
	}

	public static String[] hashTable(String[] arr) {
		String[] table = new String[9];
		int i = 0;
		while (i < arr.length) {
			int idx = hash(arr[i]) % table.length;
			if (table[idx] == null) {
				table[idx] = arr[i];
			} else {
				while (table[idx] != null) {
					idx = (idx + 1) % table.length;
				}
				table[idx] = arr[i];
			}
			i++;
		}
		return table;
	}

	public static int hash(String string) {
		int consonants = 0;
		int numericalSum = 0;
		for (int i = 0; i < string.length(); i++) {
			char ch = string.charAt(i);
			if (ch >= 48 && ch <= 57) {
				numericalSum += ch - 48;
			} else {
				if (!(ch == 65 || ch == 69 || ch == 73 || ch == 79 || ch == 85)) {
					consonants += 1;
				}
			}
		}
		// System.out.println("Num of cons: "+consonants);
		// System.out.println("Num Sum: " + numericalSum);
		return ((24 * consonants) + numericalSum) % 9;
	}

	public static void printArr(String[] arr) {
		System.out.print("[" + arr[0]);
		for (int i = 1; i < arr.length; i++) {
			System.out.print(", " + arr[i]);
		}
		System.out.print("]\n");
	}
}
