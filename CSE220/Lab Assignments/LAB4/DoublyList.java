public class DoublyList{
    public Node head;
    
    
    /* First Constructor:
     * Creates a linked list using the values from the given array. head will refer
     * to the Node that contains the element from a[0]
     */ 
    public DoublyList(Object [] a){
        
    }
    
    /* Second Constructor:
     * Sets the value of head. head will refer
     * to the given LinkedList
     */
    public DoublyList(Node h){
        head = h;
    }
    
    /* Counts the number of Nodes in the list */
    public int countNode(){
        
        return -100; // please remove this line!
    }
    
    /* prints the elements in the list */
    public void forwardprint(){    
    }
    
    public void backwardprint(){     
    }
    
    
    // returns the reference of the Node at the given index. For invalid index return null.
    public Node nodeAt(int idx){
        
        return null; // please remove this line!
    }
    
    
    
    /* returns the index of the Node containing the given element.
     *if the element does not exist in the List, return -1.
     */
    public int indexOf(Object elem){
        
        
        
        return -100; // please remove this line!
    }
    
    
    
    /* inserts Node containing the given element at the given index
     * Check validity of index.
     */
    public void insert(Object elem, int idx){
        
    }
    
    
    
    
    /* removes Node at the given index. returns element of the removed node.
     * Check validity of index. return null if index is invalid.
     */
    public Object remove(int index){
        
        
        return null; // please remove this line!
    }
    
    
    
}