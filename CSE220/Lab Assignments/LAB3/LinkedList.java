public class LinkedList {
	public Node head;

	/*
	 * First Constructor:
	 * Creates a linked list using the values from the given array. head will refer
	 * to the Node that contains the element from a[0]
	 */
	public LinkedList(Object[] a) {
		Node n = new Node(a[a.length - 1], null);
		for (int i = a.length - 2; i >= 0; i--) {
			Node nn = new Node(a[i], n);
			n = nn;
		}
		head = n;
	}

	/*
	 * Second Constructor:
	 * Sets the value of head. head will refer
	 * to the given LinkedList
	 */
	public LinkedList(Node h) {
		head = h;
	}

	/* Counts the number of Nodes in the list */
	public int countNode() {
		int count = 0;
		Node n = head;
		while (n != null) {
			count++;
			n = n.next;
		}
		return count;
	}

	/* prints the elements in the list */
	public void printList() {
		Node n = head;
		while (n.next != null) {
			System.out.print(n.element+",");
			n = n.next;
		}
		System.out.println(n.element);
	}

	// returns the reference of the Node at the given index. For invalid index
	// return null.
	public Node nodeAt(int index) {
		Node n = head;
		int count = 0;
		while (n != null) {
			if (count == index) {
				return n;
			}
			count++;
			n = n.next;
		}
		return null;
	}

	// returns the element of the Node at the given index. For invalid index return
	// null.
	public Object get(int index) {
		Node n = head;
		int count = 0;
		while (n != null) {
			if (count == index) {
				return n.element;
			}
			count++;
			n = n.next;
		}
		return null;
	}

	/*
	 * updates the element of the Node at the given index.
	 * Returns the old element that was replaced. For invalid index return null.
	 * parameter: index, new element
	 */
	public Object set(int index, Object elem) {
		Node n = head;
		int count = 0;
		while (n != null) {
			if (count == index) {
				Object temp = n.element;
				n.element = elem;
				return temp;
			}
			count++;
			n = n.next;
		}
		return null;
	}

	/*
	 * returns the index of the Node containing the given element.
	 * if the element does not exist in the List, return -1.
	 */
	public int indexOf(Object elem) {
		Node n = head;
		int count = 0;
		while (n != null) {
			if (n.element == elem) {
				return count;
			}
			count++;
			n = n.next;
		}
		return -1;
	}

	// returns true if the element exists in the List, return false otherwise.
	public boolean contains(Object elem) {
		Node n = head;
		while (n != null) {
			if (n.element == elem) {
				return true;
			}
			n = n.next;
		}
		return false;
	}

	// Makes a duplicate copy of the given List. Returns the reference of the
	// duplicate list.
	public Node copyList() {
		Node n = head;
		Node nn = new Node(n.element, null);
		Node newHead = nn;
		while (n.next != null) {
			n = n.next;
			Node nn2 = new Node(n.element, null);
			nn.next = nn2;
			nn = nn.next;
		}
		return newHead;
	}

	// Makes a reversed copy of the given List. Returns the head reference of the
	// reversed list.
	public Node reverseList() {
		Node n = head, newHead = null;
		Node nn2 = new Node(n.element, null);
		while (n.next != null) {
			n = n.next;
			Node nn = new Node(n.element, nn2);
			nn2 = nn;
			if (n.next == null) {
				newHead = nn2;
			}
		}
		return newHead;
	}

	/*
	 * inserts Node containing the given element at the given index
	 * Check validity of index.
	 */
	public void insert(Object elem, int index) {
		Node nn = new Node(elem, null);
		if (index == 0) {
			nn.next = head;
			head = nn;
		} else {
			Node n = head;
			Node prevNode = null;
			int count = 0;
			while (n != null) {
				if (count == index - 1) {
					prevNode = n;
				}
				n = n.next;
				count++;
			}
			nn.next = prevNode.next;
			prevNode.next = nn;
		}
	}

	/*
	 * removes Node at the given index. returns element of the removed node.
	 * Check validity of index. return null if index is invalid.
	 */
	public Object remove(int index) {
		Node remNode = null;
		if (index == 0) {
			remNode = head;
			head = head.next;
		} else {
			Node n = head;
			Node prevNode = null;
			int count = 0;
			while (n != null) {
				if (count == index - 1) {
					prevNode = n;
					remNode = prevNode.next;
				}
				n = n.next;
				count++;
			}
			prevNode.next =  remNode.next;
		}
		return remNode.element;
	}

	// Rotates the list to the left by 1 position.
	public void rotateLeft() {
		Node n = head;
		Node lastNode = null;
		while (n != null) {
			if (n.next == null) {
				lastNode = n;
			}
			n = n.next;
		}
		lastNode.next = head;
		lastNode = head;
		head = lastNode.next;
		lastNode.next = null;
	}

	// Rotates the list to the right by 1 position.
	public void rotateRight() {
		Node n = head;
		Node lastNode = null;
		Node prevLastNode = null;
		while (n.next != null) {
			if (n.next.next == null) {
				prevLastNode = n;
				lastNode = n.next;
			}
			n = n.next;
		}
		prevLastNode.next = null;
		lastNode.next = head;
		head = lastNode;
	}
}
