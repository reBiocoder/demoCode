class Node:
    def __init__(self, val):
        self._next = None
        self._data = val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val


def insert_data(root: Node, data: int):
    new_node = Node(data)
    tmp = root.next
    root.next = new_node
    new_node.next = tmp


def node_travel(root: Node):
    while root.next is not None:
        print(root.next.data)
        root = root.next


def isCycle(root: Node):
    p1, p2 = root, root
    while p1 is not None and p1.next is not None:
        p1 = p1.next.next
        p2 = p2.next

        if p1 == p2:
            return True
    return False


def cyclePosition(root: Node):
    p1, p2 = root, root
    while p1 is not None and p1.next is not None:
        p1 = p1.next.next
        p2 = p2.next

        if p1 == p2:
            break

    p2 = root
    while p1 is not p2:
        p1 = p1.next
        p2 = p2.next
    return p1.data


def reverseList(raw_seq: list):
    left, right = 0, len(raw_seq) - 1
    while left <= right:
        if left == right:
            break
        else:
            raw_seq[left], raw_seq[right] = raw_seq[right], raw_seq[left]
            left += 1
            right -= 1
    return raw_seq


def cir(n:int, m:int):
    def f(n, m):
        if n == 1: return 0
        else:
            return (f(n-1, m) + m) % n
    return f(n, m) + 1


if __name__ == '__main__':
    print(cir(3, 3))
    # print(reverseList([1,2,3,4,5]))

    # root = Node(0)  # 头节点
    # root.next = Node(1)
    # root.next.next = Node(2)
    # root.next.next.next = Node(3)
    # root.next.next.next.next = Node(4)
    # root.next.next.next.next.next = root.next.next
    # print(cyclePosition(root))
    # for i in range(1,5):
    #     insert_data(root, i)
    #node_travel(root)
