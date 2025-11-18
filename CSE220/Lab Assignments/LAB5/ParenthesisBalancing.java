import java.util.Scanner;

public class ParenthesisBalancing {
	public static void main(String[] args) {
		
		System.out.println();
		try (Scanner userInput = new Scanner(System.in)) {
			String expression = userInput.nextLine();
			checkBalance(expression);
		}
	}

	public static void checkBalance(String expression) {
		Stack openBracketStack = new ArrayStack();
		// Or,
		//Stack openBracketStack = new ListStack();
		int[] charPosArray = new int[expression.length()];
		int count = -1;
		boolean errorFound = false;
		for (int i = 0; i < expression.length(); i++) {
			char elem = expression.charAt(i);
			if (elem == '(' || elem == '{' || elem == '[') {
				openBracketStack.push(elem);
				count++;
				charPosArray[count] = i+1;
				//System.out.print("Pushed element: '"+elem+"', Index: "+i+" at savedIndex["+count+"]\n");
			} else if (elem == ')' || elem == '}' || elem == ']') {
				if (openBracketStack.isEmpty()) {
					errorFound = true;
					System.out.println("This expression is NOT correct.");
					System.out.print("Error at character # "+(i+1)+". '"+elem+"'-not opened.\n");
					break;
				} else {
					try {
						char openB = (char) openBracketStack.peek();
						if (openB == '(' && elem == ')' || openB == '{' && elem == '}' || openB == '[' && elem == ']') {
							//Object poped = openBracketStack.pop();
							//System.out.print("Poped element: '"+poped+"', found at savedIndex["+count+"] == "+charPosArray[count]+"\n");
							openBracketStack.pop();
							charPosArray[count] = 0;
							count--;
						} else {
							errorFound = true;
							System.out.println("This expression is NOT correct.");
							System.out.printf("Error at character # "+charPosArray[count]+". '"+openB+"'-not closed.\n");
							break;
						}
					} catch (StackUnderflowException e) {
						e.printStackTrace();
					}
				}
			}
		}
		if (errorFound == false) {
			if (!openBracketStack.isEmpty()) {
				try {
					Object openB = openBracketStack.peek();
					System.out.println("This expression is NOT correct.");
					System.out.printf("Error at character # "+charPosArray[count]+". '"+openB+"'-not closed.\n");
				} catch (StackUnderflowException e) {
					e.printStackTrace();
				}
			} else {
				System.out.println("This expression is correct.");
			}
		}
	}
}