public class DummyHeadedSinglyList {
	public Node head;

	public DummyHeadedSinglyList(Object[] a) {
		head = new Node(null, null);
		Node n = new Node(a[0], null);
		head.next = n;
		for (int i = 1; i < a.length; i++) {
			Node nn = new Node(a[i], null);
			n.next = nn;
			n = nn;
		}
	}

	public DummyHeadedSinglyList(Node h) {
		head = h;
	}

	/* prints the elements in the list */
    public void forwardprint() {
        Node n = head.next;
        while (n.next != null) {
            System.out.print(n.element + ",");
            n = n.next;
        }
        System.out.println(n.element);
    }
}
