public class Node{
	Object data;
	Node next;
	Node prev;
	
	public Node(Object d, Node a, Node p){
		data = d;
		next = a;
		prev = p;
	}
}