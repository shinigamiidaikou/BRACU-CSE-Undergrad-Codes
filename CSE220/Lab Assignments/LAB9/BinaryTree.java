import java.lang.Math;

public class BinaryTree {
	Node root = null;

	public BinaryTree(Node r) {
		root = r;
	}

	public int height() {
		return height(root);
	}
	public int height(Node n) {
		if (n == null)
			return -1;
		else {
			return 1 + Math.max(height(n.left), height(n.right));
		}
	}

	public int level(Node n) {
		if (n.parent == null) {
			return 0;
		} else {
			return 1 + level(n.parent);
		}
	}

	public void preOrderPrint() {
		preOrderPrint(root);
	}
	public void preOrderPrint(Node n) {
		if (n == null)
			return;
		else {
			System.out.print(n.element + " ");
			preOrderPrint(n.left);
			preOrderPrint(n.right);
			if (n.parent == null)
				System.out.print("\n");
		}
	}

	public void postOrderPrint() {
		postOrderPrint(root);
	}
	public void postOrderPrint(Node n) {
		if (n == null) {
			return;
		} else {
			postOrderPrint(n.left);
			postOrderPrint(n.right);
			System.out.print(n.element + " ");
			if (n.parent == null)
				System.out.print("\n");
		}
	}

	public void inOrderPrint() {
		inOrderPrint(root);
	}
	public void inOrderPrint(Node n) {
		if (n == null) {
			return;
		} else {
			inOrderPrint(n.left);
			System.out.print(n.element + " ");
			inOrderPrint(n.right);
			if (n.parent == null)
				System.out.print("\n");
		}
	}

	public static void main(String[] args) {
		Node n0 = new Node("A", null, null, null);
		Node n1 = new Node("B", null, null, n0);
		Node n2 = new Node("C", null, null, n0);
		n0.left = n1;
		n0.right = n2;
		Node n3 = new Node("D", null, null, n2);
		Node n4 = new Node("E", null, null, n2);
		n2.left = n3;
		n2.right = n4;
		Node n5 = new Node("F", null, null, n3);
		n3.left = n5;

		BinaryTree t1 = new BinaryTree(n0);
		System.out.println(t1.height());
		System.out.println(t1.level(n3));
		t1.preOrderPrint();
		t1.postOrderPrint();
		t1.inOrderPrint();
	}
}
