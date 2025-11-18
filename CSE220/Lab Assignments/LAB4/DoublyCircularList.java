public class DoublyCircularList {
    public Node head;

    /*
     * First Constructor:
     * Creates a linked list using the values from the given array. head will refer
     * to the Node that contains the element from a[0]
     */
    public DoublyCircularList(Object[] a) {
        head = new Node(a[0], null, null);
        Node n = head;
        for (int i = 1; i < a.length; i++) {
            Node nn = new Node(a[i], null, n);
            n.next = nn;
            n = nn;
        }
        n.next = head;
        head.prev = n;
    }

    /*
     * Second Constructor:
     * Sets the value of head. head will refer
     * to the given LinkedList
     */
    public DoublyCircularList(Node h) {
        head = h;
    }

    /* Counts the number of Nodes in the list */
    public int countNode() {
        int count = 1;
        Node n = head.next;
        while (n != head){
            count++;
            n = n.next;
        }
        return count;
    }

    /* prints the elements in the list */
    public void forwardprint() {
        Node n = head;
        if (n.next == head) {
            System.out.println(n.element);
        }
        else {
            while (n.next != head) {
                System.out.print(n.element + ",");
                n = n.next;
            }
            System.out.println(n.element);
        }
    }

    public void backwardprint() {
        Node n = head;
        if (n.prev == head) {
            System.out.println(n.element);
        }
        else {
            n = n.prev;
            while (n != head) {
                System.out.print(n.element + ",");
                n = n.prev;
            }
            System.out.println(n.element);
        }
    }

    // returns the reference of the Node at the given index. For invalid index
    // return null.
    public Node nodeAt(int idx) {
        if (idx == 0) {
            return head;
        }
        else {
            Node n = head.next;
            int count = 1;
            while (n != head) {
                if (count == idx) {
                    return n;
                }
                count++;
                n = n.next;
            }
            return null;
        }
    }

    /*
     * returns the index of the Node containing the given element.
     * if the element does not exist in the List, return -1.
     */
    public int indexOf(Object elem) {
        if (head.element == elem) {
            return 0;
        }
        else {
            Node n = head.next;
            int count = 1;
            while (n != head) {
                if (n.element == elem) {
                    return count;
                }
                count++;
                n = n.next;
            }
            return -1;
        }
    }

    /*
     * inserts Node containing the given element at the given index
     * Check validity of index.
     */
    public void insert(Object elem, int idx) {
        int size = 1;
        Node n = head.next;
        while (n != head){
            size++;
            n = n.next;
        }
        if (idx < 0 || idx > size) {
            new IndexOutOfBoundsException("Index must be greater or equal to zero and less or equal to size");
        } else {
            if (idx == 0) {
                Node nn = new Node(elem, head, head.prev);
                head.prev.next = nn;
                head.prev = nn;
                head = nn;
            }
            else {
                n = head.next;
                for (int i = 1; i <= size; i++) {
                    if (i == idx) {
                        Node nn = new Node(elem, n, n.prev);
                        n.prev.next = nn;
                        n.prev = nn;
                    }
                    n = n.next;
                }
            }
        }
    }

    /*
     * removes Node at the given index. returns element of the removed node.
     * Check validity of index. return null if index is invalid.
     */
    public Object remove(int index) {
        int size = 1;
        Node n = head.next;
        while (n != head){
            size++;
            n = n.next;
        }
        if (index < 0 || index >= size) {
            return null;
        } else {
            if (index == 0) {
                Object removed = head.element;
                head.prev.next = head.next;
                head.next.prev = head.prev;
                head = head.next;
                return removed;
            }
            else {
                n = head.next;
                for (int i = 1; i <= size; i++) {
                    if (i == index) {
                        n.prev.next = n.next;
                        n.next.prev = n.prev;
                        return n.element;
                    }
                    n = n.next;
                }
                return null;
            }
        }
    }

}