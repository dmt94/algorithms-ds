//traversal

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
};

const a = new Node('A');
const b = new Node('B');
const c = new Node('C');
const d = new Node('D');

//linking list together
a.next = b;
b.next = c;
c.next = d;

//  A -> B -> C -> D -> NULL
// head

const printLinkedList = (head) => {
  if (head === null) return;
  console.log(head.val);
  // make a recursive call on the next value
  printLinkedList(head.next);
};

printLinkedList(a);