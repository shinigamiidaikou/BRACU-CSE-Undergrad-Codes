public class ArrayStack implements Stack{
	private int top;
	private Object[] mainArr;

	// Array default initial capacity
	private static final int DEF_INIT_CAPACITY = 50;

	public ArrayStack() {
		mainArr = new Object[DEF_INIT_CAPACITY];
		top = -1;
	}
	
	public void push(Object data) {
		try {
			top++;
			mainArr[top] = data;
		} catch (ArrayIndexOutOfBoundsException e) {
			Object[] tmpArray = new Object[mainArr.length * 2];
			for (int i = 0; i < mainArr.length; i++) {
				tmpArray[i] = mainArr[i];
			}
			mainArr = tmpArray;
			mainArr[top] = data;
		}
	}

	public Object pop() throws StackUnderflowException {
		try {
			Object elem = mainArr[top];
			mainArr[top] = null;
			top--;
			return elem;
		} catch (ArrayIndexOutOfBoundsException e) {
			throw new StackUnderflowException(e);
		}
	}

	public Object peek() throws StackUnderflowException {
		try {
			return mainArr[top];
		} catch (ArrayIndexOutOfBoundsException e) {
			throw new StackUnderflowException(e);
		}
	}

	public boolean isEmpty() {
		if (top == -1) {
			return true;
		}
		return false;
	}
}