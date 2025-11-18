class Node {
	Object element;
	Node next;

	Node(Object e, Node n) {
		element = e;
		next = n;
	}
}

class singlyList {
	Node head;

	singlyList(Object[] arr) {
		if (arr.length == 0) {
			head = new Node(null, null);
			return;
		}
		Node n = new Node(arr[arr.length - 1], null);
		for (int i = arr.length - 2; i >= 0; i--) {
			Node nn = new Node(arr[i], n);
			n = nn;
		}
		head = n;
	}

	singlyList(Node h) {
		head = h;
	}
}

public class Lab6_2 {
	public static void main(String[] args) {
		Object[] arr1 = { 1, 2, 3, 4, 5 };
		singlyList list1 = new singlyList(arr1);
		System.out.println("List Summ = " + listSumm(list1.head));
		printBackward(list1.head);
		String bin = decimalToBinary(232);
		System.out.println(bin);
	}

	public static String decimalToBinary(int n) {
		if (n == 0) {
			return "0";
		} else if (n == 1) {
			return "1";
		} else {
			return decimalToBinary(n / 2) + (n % 2);
		}
	}

	public static int listSumm(Node head) {
		if (head.next == null) {
			if (head.element == null) {
				return 0;
			}
			return (int) head.element;
		} else {
			return (int) head.element + (int) listSumm(head.next);
		}
	}

	public static void printBackward(Node head) {
		if (head.next == null) {
			System.out.println(head.element);
		} else {
			printBackward(head.next);
			System.out.println(head.element);
		}
	}
}
