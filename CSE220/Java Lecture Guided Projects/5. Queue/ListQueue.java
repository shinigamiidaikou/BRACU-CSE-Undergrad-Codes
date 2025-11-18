class Node {
	Node next;
	Object element;

	Node (Object e, Node n) {
		element = e;
		next = n;
	}
}

public class ListQueue implements Queue {
	private Node head; // Reference to the front of the queue
	private int size; // The number of items in the queue
	public ListQueue() {
	head = null;
	size = 0;
	}
	// The rest of the implementation goes here...
	@Override
	public int size() {
		// TODO Auto-generated method stub
		return 0;
	}
	@Override
	public boolean isEmpty() {
		// TODO Auto-generated method stub
		return false;
	}
	@Override
	public void enqueue(Object o) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public Object dequeue() throws QueueUnderflowException {
		// TODO Auto-generated method stub
		return null;
	}
	@Override
	public Object peek() throws QueueUnderflowException {
		// TODO Auto-generated method stub
		return null;
	}
	@Override
	public Object[] toArray() {
		// TODO Auto-generated method stub
		return null;
	}
	@Override
	public int search(Object o) {
		// TODO Auto-generated method stub
		return 0;
	}
	}