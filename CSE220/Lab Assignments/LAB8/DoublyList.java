class Node {
	Object element;
	Node next;
	Node prev;

	Node (Object e, Node n, Node p) {
		element = e;
		next = n;
		prev = p;
	}
}

public class DoublyList {
	Node head;

	public DoublyList (Object[] arr) {
		if (arr.length == 0) {
			head = new Node(null,null,null);
			return;
		}
		head = new Node(arr[0], null, null);
		Node n = head;
		for (int i = 1; i < arr.length; i++) {
			Node nn = new Node(arr[i], null, n);
			n.next = nn;
			n = nn;
		}
	}

	public DoublyList (Node h) {
		head = h;
	}

	

}