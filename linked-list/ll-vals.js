// const linkedListValues = (head) => {
//   const values = [];
//   let current = head;
//   //assures that every node is processed
//   while (current !== null) {
//     values.push(current.val);
//     current = current.next;
//   }
//   return values;
// }

//recursive version
const linkedListValues = (head) => {
  const values = [];
  //arrays and objects are pass by reference
  fillValues(head, values);
  return values;
};

const fillValues = (head, values) => {
  if (head === null) return;
  values.push(head.val);
  fillValues(head.next, values);
};

// best to split it in two function,
// so that recursive function 
// doesn't have to create multiple arrays, which would be quadratic runtime