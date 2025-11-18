class Node {
	Object element;
	Node next;

	Node (Object e, Node n) {
		element = e;
		next = n;
	}
}

public class SinglyList {
	Node head;

	public SinglyList (Object[] arr) {
		if (arr.length == 0) {
			head = new Node(null, null);
			return;
		}
		head = new Node(arr[0], null);
		Node n = head;
		for (int i = 1; i < arr.length; i++) {
			Node nn = new Node(arr[i], null);
			n.next = nn;
			n = nn;
		}
	}

	public SinglyList(Node h) {
		head = h;
	}

	public void selectionSort() {
		selectionSort(head);
	}
	public void selectionSort(Node head) {
		
	}

}
