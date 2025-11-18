public class ListSumTester {
	public static void main(String[] args) {

		Object[] a1 = { 9, 9, 4, 6, 3 };
		DummyHeadedSinglyList h1 = new DummyHeadedSinglyList(a1);

		Object[] a2 = { 9, 5, 2 };
		DummyHeadedSinglyList h2 = new DummyHeadedSinglyList(a2);

		Node sum1head = listItemsSumm(h1.head, h2.head);
		DummyHeadedSinglyList sum1list = new DummyHeadedSinglyList(sum1head);

		sum1list.forwardprint();
	}

	public static Node listItemsSumm(Node head1, Node head2) {
		Node n, nn2;

		n = head1.next;
		nn2 = new Node(n.element, null);
		n = n.next;
		while (n != null) {
			Node nn = new Node(n.element, nn2);
			nn2 = nn;
			n = n.next;
		}
		Node n1 = nn2;
		DummyHeadedSinglyList new1 = new DummyHeadedSinglyList(new Node(null, n1));
		new1.forwardprint();

		n = head2.next;
		nn2 = new Node(n.element, null);
		n = n.next;
		while (n != null) {
			Node nn = new Node(n.element, nn2);
			nn2 = nn;
			n = n.next;
		}
		Node n2 = nn2;
		DummyHeadedSinglyList new2 = new DummyHeadedSinglyList(new Node(null, n2));
		new2.forwardprint();
		
		int hand = 0;
		int newElem = (int) n1.element + (int) n2.element;
		if (newElem > 9) {
			hand = 1;
			newElem = newElem - 10;
		}
		Node sumNode2 = new Node(newElem, null);
		n1 = n1.next;
		n2 = n2.next;
		while (true) {
			if (n1 == null || n2 == null) {
				if (n1 == null && n2 == null) {
					break;
				} else if (n1 == null) {
					newElem = (int) n2.element + hand;
					if (newElem > 9) {
						newElem = newElem - 10;
						hand = 1;
					} else hand = 0;
					Node sumNode = new Node(newElem, sumNode2);
					sumNode2 = sumNode;
					n2 = n2.next;
					continue;
				} else {
					newElem = (int) n1.element + hand;
					if (newElem > 9) {
						newElem = newElem - 10;
						hand = 1;
					} else hand = 0;
					Node sumNode = new Node(newElem, sumNode2);
					sumNode2 = sumNode;
					n1 = n1.next;
					continue;
				}
			}
			newElem = (int) n1.element + (int) n2.element + hand;
			if (newElem > 9) {
				newElem = newElem - 10;
				hand = 1;
			} else hand = 0;
			Node sumNode = new Node(newElem, sumNode2);
			sumNode2 = sumNode;
			n1 = n1.next;
			n2 = n2.next;
		}
		if (hand == 1) {
			Node sumNode = new Node(1, sumNode2);
			sumNode2 = sumNode;
		}
		Node sumHead = new Node(null, sumNode2);
		return sumHead;
	}
}
