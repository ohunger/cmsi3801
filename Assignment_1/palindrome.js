class Node {
    constructor(val) {
        this.data = val;
        this.next = null;
    }
}

const palindrome = (head) => {
    if (!head || !head.next) {
        return true; 
    }//empty or one letter

    let fast = head, slow = head;
    const stack = [];

    while (fast && fast.next) {
        stack.push(slow.data);
        fast = fast.next.next;
        slow = slow.next; 
    }//push first half of linked list onto stack

    if (fast) { // if list has odd number of elements move slow past middle
        slow = slow.next;
    }

    //going to compare stack aka first half with rest aka slow
    while (slow) {
        const pop = stack.pop();
        if (pop !== slow.data) {
          return false;
        }
        slow = slow.next;
    }
    return true;
}


let head = new Node("a")
head.next = new Node("b")
head.next = new Node("a")
console.log("aba " + palindrome(head));

let head2 = new Node("c")
head2.next = new Node("a")
head2.next = new Node("t")
console.log("cat " + palindrome(head2));