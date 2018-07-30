

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data


# 定义链表操作类(所有节点都先经过 Node 类处理过)
class LinkedList(object):
    # 初始化一个头结点
    def __init__(self, head):
        self.head = head

    # 获取链表的长度
    def getLen(self):
        length = 0
        temp = self.head
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    # 追加节点(传进来的是一个处理过的节点)
    def add(self, node):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    # 删除节点(关键是找到要删除节点的前一个节点)
    def delete(self, index):
        if index < 1 or index > self.getLen():
            print("index is out of range")
            return False
        # 如果删除的是头结点
        if index == 1:
            self.head = self.head.next
        position = 0
        temp = self.head
        while temp is not None:
            position += 1
            if position == index-1:
                temp.next = temp.next.next
                break
            temp = temp.next

    # 插入节点
    def insert(self, index, node):
        if index < 1 or index > self.getLen():
            print("index is out of range")
            return False
        position = 0
        temp = self.head
        while temp is not None:
            position += 1
            if position == index-1:
                node.next = temp.next
                temp.next = node
                break
            temp = temp.next

    # 打印链表
    def printList(self, head):
        lists = []
        while head is not None:
            lists.append(head.getData())
            head = head.next
        return lists


if __name__ == '__main__':
    head = Node("head")
    linked_list = LinkedList(head)
    for i in range(10):
        node = Node(i)
        linked_list.add(node)
    print(linked_list.printList(head))
    linked_list.delete(5)
    print(linked_list.printList(head))
    a = Node("add")
    linked_list.add(a)
    print(linked_list.printList(head))
    node = Node("insert")
    linked_list.insert(4, node)
    print(linked_list.printList(head))
