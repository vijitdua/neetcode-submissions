class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.start = None

    # index = -1 means get tail
    # return None if index out of bounds
    def get_node(self, index: int):
        i = 0
        current_node = self.start
        if not current_node:
            return None
        while current_node.next != None and (i < index or index == -1):
            current_node = current_node.next
            i += 1
        if index == -1:
            return current_node
        return current_node if i == index else None

    def get(self, index: int) -> int:
        node = self.get_node(index)
        return node.data if node else -1

    def insertHead(self, val: int) -> None:
        new_head = Node(val, self.start)
        self.start = new_head

    def insertTail(self, val: int) -> None:
        if not self.start:
            self.insertHead(val)
            return
        else:
            current_tail_node = self.get_node(-1)
            new_tail = Node(val, None)
            current_tail_node.next = new_tail

    def remove(self, index: int) -> bool:
        node_to_remove = self.get_node(index)
        if (node_to_remove == None):
            return False
        if index == 0: 
            self.start = node_to_remove.next
        else:
            node_before_removal_node = self.get_node(index-1)
            node_before_removal_node.next = node_to_remove.next
        del node_to_remove
        return True

    def getValues(self) -> List[int]:
        current_node = self.start
        output = []
        while (current_node != None):
            output.append(current_node.data)
            current_node = current_node.next
        return output
