class Node {
	Object element;
	Node next;

	Node(Object e, Node n) {
		element = e;
		next = n;
	}
}

public class ListStack implements Stack {
	private Node top;

	public ListStack() {
		top = null;
	}

	public void push(Object data) {
		top = new Node(data, top);
	}

	public Object pop() throws StackUnderflowException {
		try {
			Object elem = top.element;
			top = top.next;
			return elem;
		} catch (NullPointerException e) {
			throw new StackUnderflowException(e);
		}
	}

	public Object peek() throws StackUnderflowException {
		try {
			return top.element;
		} catch (NullPointerException e) {
			throw new StackUnderflowException(e);
		}
	}

	public boolean isEmpty() {
		if (top == null) {
			return true;
		}
		return false;
	}
}
