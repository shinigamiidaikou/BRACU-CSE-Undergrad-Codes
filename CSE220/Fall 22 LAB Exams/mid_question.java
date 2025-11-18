class Node {
	Object element;
	Node next;

	Node(Object d, Node n) {
		element = d;
		next = n;
	}
}

class List {
	Node head;

	List(Object[] arr) {
		head = new Node(arr[0], null);
		Node n = head;
		for (int i = 1; i < arr.length; i++) {
			Node nn = new Node(arr[i], null);
			n.next = nn;
			n = nn;
		}
	}

	List(Node h) {
		head = h;
	}

	void printForward() {
		if (head.next == null) {
			System.out.println(head.element);
		} else {
			Node n = head;
			while (n.next != null) {
				System.out.print(n.element + " --> ");
				n = n.next;
			}
			System.out.println(n.element);
		}
	}

	void add(List list2) {
		Node n = head;
		while (n.next != null) {
			n = n.next;
		}
		n.next = list2.head;
	}

	List reverse() {
		Node nn2 = new Node(head.element, null);
		Node n = head.next;
		while (n != null) {
			Node nn = new Node(n.element, nn2);
			nn2 = nn;
			n = n.next;
		}
		return new List(nn2);
	}
}

public class LABMID {
	public static void main(String[] args) {

		Object[] arr1 = { 1, 3, 2, 4 };
		Object[] arr2 = { 7, 2, 6, 5 };
		Object[] arr3 = { 2, 0, 0, 5 };
		List list1 = new List(arr1);
		List list2 = new List(arr2);
		List list3 = new List(arr3);
		list1.printForward();
		list2.printForward();
		list3.printForward();
		System.out.println();
		List idList = idGenerator(list1, list2, list3);
		idList.printForward();
	}

	public static List idGenerator(List list1, List list2, List list3) {
		List reverserList2 = list2.reverse();
		List reverserList3 = list3.reverse();

		Node n1 = list1.head;
		Node n2 = reverserList3.head;
		Node n = new Node(((int) n1.element + (int) n2.element) % 10, null);
		List sumList = new List(n);
		n1 = n1.next;
		n2 = n2.next;
		while (n1 != null) {
			Node nn = new Node(((int) n1.element + (int) n2.element) % 10, null);
			n.next = nn;
			n = nn;
			n1 = n1.next;
			n2 = n2.next;
		}
		reverserList2.add(sumList);
		return reverserList2;
	}
}