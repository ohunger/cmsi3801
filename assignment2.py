class ListNode:
    def __init__(self, value):
        self.next = None
        self.value = value
        
def string_compression(s):
    count = 1

    compressed = []

    for i in range(1, len(s)):
        if s[i - 1] == s[i] :
            count += 1

        else:
            compressed.append(s[i - 1])
            compressed.append(str(count))
            #reset count
            count = 1

    compressed.append(s[-1])
    #append conpressed amt
    compressed.append(str(count))

    compressed_str = ''.join(compressed)
    #checkcase for if its og
    return compressed_str if len(compressed_str) < len(s) else s

def add_linked_lists_reverse(l1, l2):
    carry = 0

    dummy_head = ListNode(0)
    current = dummy_head

    while l1 or l2:
        x = l1.value if l1 else 0
        y = l2.value if l2 else 0

        total = x + y + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next

def delete_middle_node(node):
    if node is None or node.next is None:
        return False
    #first checking
    next_node = node.next
    #temporary nextnode, point og node to temp node


    node.value = next_node.value
    node.next = next_node.next
    return True

class StackWithMin:
    def __init__(self):
        #using a secondary list to make this work
        self.min_stack = []
        self.stack = []
    #basically just adding simple pop and push functions from regular stack
    def pop(self):
        if not self.stack:
            return None
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
    
    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

def main():
    # I tried to use test cases given to us by the book.
    print("Test String Compression") 
    input_str = "aabcccccaaa"
    compressed_str = string_compression(input_str)
    print("String Compression:", compressed_str)

    print("Test delete mid node")
    # I was too lazy to implement a linked list class so Im just manually make
    # a linked list using nextnodes
    a = ListNode("a")
    b = ListNode("b")
    c = ListNode("c")
    d = ListNode("d")
    e = ListNode("e")
    f = ListNode("f")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    node_to_delete = c
    delete_middle_node(node_to_delete)

    current_node = a
    print("Delete Middle Node:")
    while current_node:
        print(current_node.value, end=" -> ")
        current_node = current_node.next
    print("None")

    print(" Test Sum Lists (Reverse)")
    l1 = ListNode(7)
    l1.next = ListNode(1)
    l1.next.next = ListNode(6)

    l2 = ListNode(5)
    l2.next = ListNode(9)
    l2.next.next = ListNode(2)

    result = add_linked_lists_reverse(l1, l2)
    current = result
    print("Sum Lists (Reverse Order):")
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

    print("Test Stack Min") 
    stack = StackWithMin()
    stack.push(5)
    stack.push(2)
    stack.push(4)
    stack.push(1)

    print("Stack Min:")
    print("Current stack:", stack.stack)
    print("Minimum element:", stack.min())

    stack.pop()
    stack.pop()

    print("Current stack:", stack.stack)
    print("Minimum element:", stack.min())

if __name__ == "__main__":
    main()