public class DoublyLinkedList {
	Node head;

	public DoublyLinkedList(Object[] a){
		head = new Node(10, null, null);
	}

	public DoublyLinkedList(Node h){
		head = h;
	}
}