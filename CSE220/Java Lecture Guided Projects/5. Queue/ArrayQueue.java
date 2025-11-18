import java.util.Arrays;

public class ArrayQueue implements Queue {
	private Object[] data; // The array container
	private int front; // The index of the front item
	private int size; // The number of items in the queue

	// Default initial capacity, which may then dynamically change
	private static final int DEF_INIT_CAPACITY = 100;

	public ArrayQueue() {
		data = new Object[DEF_INIT_CAPACITY];
		front = 0;
		size = 0;
	}

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

	@Override
	public String toString() {
		return "ArrayQueue [data=" + Arrays.toString(data) + ", front=" + front + ", size=" + size + "]";
	}
}