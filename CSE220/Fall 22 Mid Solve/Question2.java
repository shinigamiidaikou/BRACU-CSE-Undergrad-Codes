public class Question2 {

	public static void main(String[] args) {
		int[] arr = { 1, 2, 3, 4, 5, 6 };
		Question2 q2 = new Question2();
		Node head1 = q2.singlyList(arr);
		q2.forwardPrint(head1);
		System.out.println("Last N Node Sum: "+ q2.sumOfLastNNodes(head1, 6, 6));
	}

	public Node singlyList(int[] arr) {
		Node nn2 = new Node(arr[arr.length - 1], null);
		for (int i = arr.length - 2; i >= 0; i--) {
			Node nn = new Node(arr[i], nn2);
			nn2 = nn;
		}
		return nn2;
	}

	public void forwardPrint(Node head) {
		if (head == null) {
			System.out.println("null");
		} else if (head.next == null) {
			System.out.println(head.element);
		} else {
			System.out.print(head.element + " --> ");
			Node n = head.next;
			while(n.next != null) {
				System.out.print(n.element + " --> ");
				n = n.next;
			}
			System.out.println(n.element);
		}
	}

	public int sumOfLastNNodes(Node head, int size, int N) {
		if (N < 0 || N > size) {
			return -1;
		}
		Node nn2 = new Node(head.element, null);
		Node n = head.next;
		while (n != null) {
			Node nn = new Node(n.element, nn2);
			nn2 = nn;
			n = n.next;
		}
		n = nn2; // new reversed list head node in nn2
		int NSum = 0, count = 0;
		while (count < N) {
			NSum = NSum + (int) n.element;
			count++;
			n = n.next;
		}
		return NSum;
	}
}
