#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-09 13:03:04
# @Author  : mohailang (1198534595@qq.com)

# 在 Python 里，用 list对象以及其方法就可以简单实现堆栈和队列了
# 但为了理解，还是用 Python 来模拟具体实现这两种数据结构
# -*- 队列、堆栈 begin -*-


class Queue(object):
    """队列类: 先进先出"""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """入队"""
        self.items.append(item)

    def dequeue(self):
        """出队"""
        self.items.pop(0)

    def size(self):
        """队列大小"""
        return len(self.items)

    def isEmpty(self):
        """判断队列是否为空"""
        return self.size() == 0


class Stack (object):
    """堆栈类: 后进先出"""

    def __init__(self):
        self.items = []

    def push(self, item):
        """ 压栈"""
        self.items.append(item)

    def pop(self):
        """出栈"""
        return self.items.pop()

    def size(self):
        """堆栈大小"""
        return len(self.items)

    def top(self):
        """返回栈顶元素"""
        return self.items[self.size()-1]

    def isEmpty(self):
        """判断堆栈是否为空"""
        return self.size() == 0


# -*- 链表 begin -*-


# 定义链表节点类
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

    # 反转链表
    def listReverse(self, head):
        if head.next is None:
            return head
        pre = head
        cur = head.next
        while cur is not None:
            # 断链前先保存后面的节点
            temp = cur.next
            # 断链，把当前节点指向前一个节点
            cur.next = pre
            # 把节点不断往后移一位，把当前节点作为下一次的前一个节点，把后一个节点作为下次的当前节点，不断迭代
            pre = cur
            cur = temp
        head.next = None
        # 返回反转后的头结点
        return pre


if __name__ == '__main__':
    print("\n链表:")
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
    head = linked_list.listReverse(head)
    print(linked_list.printList(head))


# -*- 链表 end -*-


# -* 图 begin -*
a, b, c, e, f = range(5)
# 邻接列表
N = [
    [b, c],
    [a, c],
    [a, b, e, f],
    [c, f],
    [c, e]
]
# 加权邻接字典
N = [
    {'b': 2, 'c': 3, 'f': 2},   # a
    {'a': 2, 'c': 2},  # b
    {'a': 3, 'b': 2, 'e': 4, 'f': 3},  # c
    {'c': 4, 'f': 5},  # e
    {'c': 3, 'e': 5}  # f
]
# 邻接集的字典表示法
N = {
    'a': set('bc'),
    'b': set('a,c'),
    'c': set('a,b,e,f'),
    'e': set('c,f'),
    'f': set('c,e')
}
# 邻接矩阵(用1和0来表示相关节点是否为当前节点的邻居)
N = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0]
]
# 对不存在的边赋予无限大权值的加权矩阵
inf = float('inf')
N = [
    [0, 1, 1, inf, 1],
    [1, 0, 1, inf, inf],
    [1, 1, 0, 1, 1],
    [inf, inf, 1, 0, 1],
    [inf, inf, 1, 1, 0]
]


# -*- 图  end -*-
class Vertex(object):
    """ 定义顶点"""

    def __init__(self, key):
        self.ID = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=None):
        """添加邻接顶点"""
        self.connectedTo[nbr] = weight

    def getConnections(self):
        """获取其所有邻接顶点"""
        return self.connectedTo.keys()  # 结合下文，这里keys 都是对象来的

    def getID(self):
        """获取其ID"""
        return self.ID

    def getWeight(self, nbr):
        """获取与其邻接的邻居之间的权重值"""
        return self.connectedTo[nbr]


class Graph(object):
    """定义一个图"""

    def __init__(self):
        self.vertexList = {}  # 保存图中的每一个顶点对象(包括对象之间的关系)
        self.vertexNum = 0  # 记录顶点数目

    def addVertex(self, key):
        """创建孤儿顶点对象并加到图中"""
        self.vertexNum += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def addEdge(self, vertex1, vertex2, weight):
        """连接两个顶点：vertex1->vertex2"""
        if vertex1 not in self.vertexList:
            self.addVertex(vertex1)
        if vertex2 not in self.vertexList:
            self.addVertex(vertex2)
        self.vertexList[vertex1].addNeighbor(self.vertexList[vertex2], weight)

    def getVertex(self, key):
        """获取顶点对象"""
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None

    def getVertices(self):
        """获取所有顶点的名称"""
        return self.vertexList.keys()

    def __iter__(self):
        """把这个类设置为可迭代"""
        return iter(self.vertexList.values())


# 深度优先搜索实现步骤：
# （1）访问初始顶点 v 并标记顶点v已访问。
# （2）查找顶点 v 的第一个邻接顶点w。
# （3）若顶点v 的邻接顶点w存在，则继续执行；否则回溯到v，再找v的另外一个未访问过的邻接点。
# （4）若顶点w尚未被访问，则访问顶点w 并标记顶点w为已访问。
# （5）继续查找顶点w 的下一个邻接顶点wi，如果v 取值wi转到步骤（3）。直到连通图中所有顶点全部访问过为止。

    dfsVisited = []   # 记录被访问过的顶点,也就是深度优先搜索的路径

    def dfs(self, root):
        """深度优先搜索"""
        # 获取该顶点的所有邻接顶点，对其进行深度优先遍历
        connections = self.vertexList[root].getConnections()
        if root not in self.dfsVisited:
            self.dfsVisited.append(root)
            # print(root, end=' ')
            for neighbor in connections:
                self.dfs(neighbor.getID())
        return self.dfsVisited

    bfsVisited = []  # 记录被访问过的顶点,也就是深度优先搜索的路径

    def bfs(self, root):
        """ 广度优先搜索"""
        queue = []  # 队列，先进先出，
        queue.append(root)
        self.bfsVisited.append(root)
        while len(queue):  # 当队列里还有元素的时候，说明还有顶点未被访问
            vertex = queue.pop(0)  # 把先进的元素提取出来先处理
            for neighbor in self.vertexList[vertex].getConnections():
                if neighbor.getID() not in self.bfsVisited:
                    self.bfsVisited.append(neighbor.getID())
                    queue.append(neighbor.getID())  # 后进的元素
        return self.bfsVisited


if __name__ == '__main__':
    print("\n图：")
    graph = Graph()
    for vertex in range(6):
        graph.addVertex(vertex)
    graph.addEdge(0, 1, 5)
    graph.addEdge(0, 5, 2)
    graph.addEdge(1, 2, 4)
    graph.addEdge(2, 3, 9)
    graph.addEdge(3, 4, 7)
    graph.addEdge(3, 5, 3)
    graph.addEdge(4, 0, 1)
    graph.addEdge(5, 4, 8)
    graph.addEdge(5, 2, 1)
    print(graph.vertexList)  # 顶点
    # 打印图
    for vertex in graph:
        for neighbor in vertex.getConnections():
            print("( %s -> %s weight: %d)" %
                  (vertex.getID(), neighbor.getID(), vertex.getWeight(neighbor)))
    print(graph.dfs(3))
    print(graph.bfs(3))


# -*- 二叉树 begin -*-
# 前序遍历：根结点->左子树->右子树
# 中序遍历：左子树->根结点->右子树
# 后序遍历：左子树->右子树->根结点


class Node(object):
    """节点类"""

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree(object):
    """定义二叉树类"""

    def __init__(self):
        self.root = Node()
        self.nodeList = []  # 用以存放相对的父节点，用以开辟其子节点

    def add(self, value):
        """添加节点"""
        node = Node(value)
        if self.root.value == None:  # 判断树是否是空的
            self.root = node
            self.nodeList.append(self.root)
        else:
            parentNode = self.nodeList[0]  # 给nodeList里面相对的父节点添加其子节点
            if parentNode.left == None:
                parentNode.left = node
                self.nodeList.append(parentNode.left)
            else:
                parentNode.right = node
                self.nodeList.append(parentNode.right)
                # 此时parentNode 已有两个节点，所以对它的构造完成，移除它
                self.nodeList.pop(0)

    def frontSearch(self, root):
        """递归前序遍历"""
        if root == None:
            return False
        print(root.value, end=' '),
        self.frontSearch(root.left)
        self.frontSearch(root.right)

    def midSearch(self, root):
        """递归中序遍历"""
        if root == None:
            return False
        self.midSearch(root.left)
        print(root.value, end=' '),
        self.midSearch(root.right)

    def backSearch(self, root):
        """递归后序遍历"""
        if root == None:
            return False
        self.backSearch(root.left)
        self.backSearch(root.right)
        print(root.value, end=' ')

    def frontStack(self, root):
        """利用堆栈前序遍历"""
        if root == None:
            return False
        stack = []
        node = root
        while node or stack:
            while node:  # 寻找左子树，压入栈内
                print(node.value, end=' ')
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right  # 开始寻找右子树

    def midStack(self, root):
        """ 利用堆栈中序遍历"""
        if root == None:
            return False
        stack = []
        node = root
        while node or stack:
            while node:  # 从根结点开始，寻找左子树，把它压入栈中
                stack.append(node)
                node = node.left
            node = stack.pop()  # while 结束代表前一个节点没有了左子树
            print(node.value, end=' ')
            node = node.right  # 然后开始寻找右子树

    def backStack(self, root):
        """利用堆栈后序遍历"""
        if root is None:
            return False
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:   # 找出后序遍历的逆序，存放在 stack2中
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:  # 将 stack2中的元素出栈，即是后序遍历序列
            print(stack2.pop().value, end=' ')

    def levelSearch(self, root):
        """层序遍历"""
        if root is None:
            return False
        treeList = []
        treeList.append(root)
        while treeList:
            node = treeList.pop(0)  # 先进先出
            print(node.value, end=' ')
            if node.left:
                treeList.append(node.left)
            if node.right:
                treeList.append(node.right)


if __name__ == '__main__':
    print("\n树:")
    tree = Tree()
    for node in range(10):
        tree.add(node)
    tree.levelSearch(tree.root)
    print()
    tree.frontSearch(tree.root)
    print()
    tree.midSearch(tree.root)
    print()
    tree.backSearch(tree.root)
    print()
    tree.frontStack(tree.root)
    print()
    tree.midStack(tree.root)
    print()
    tree.backStack(tree.root)
    print()


# 冒泡排序
# 1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
# 3.针对所有的元素重复以上的步骤，除了最后一个。
# 4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
L = [3, 5, 6, 7, 8, 1, 2]
for i in range(len(L) - 1):
    for j in range(len(L) - 1 - i):
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
print(L)


# 快速排序
# 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后
# 再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j - 1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i + 1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i - 1)
    quickSort(L, j + 1, high)
    return L


# 桶排序
# 将数组分到有限数量的桶子里。每个桶子再个别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）


# 基数排序
# 先对比数组中每个数的低位，分到不同的"桶子"里，再把它们重新串接起来，然后继续比较高一位，重复步骤，最后把它们
# 串接起来就是有序的序列了


# 堆排序
# 将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，
# 此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)


def build_heap(lists, size):
    for i in range(0, (size / 2))[::-1]:
        adjust_heap(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
