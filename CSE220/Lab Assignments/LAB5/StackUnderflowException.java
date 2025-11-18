public class StackUnderflowException extends Exception{
	public StackUnderflowException(Throwable err) {
		super("Stack Empty!", err);
    }
}