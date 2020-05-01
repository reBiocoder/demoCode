class Node:
    """节点类"""
    def __init__(self, elem, lchild=None, rchild=None):
        self.val = elem
        self.left = lchild
        self.right = rchild


class Tree:
    """树类"""
    def __init__(self, root=None):
        self._root = root

    def add(self, item):
        node = Node(item)
        if not self._root:
            self._root = node
            return
        queue = [self._root]
        while queue:
            cur = queue.pop(0)
            if not cur.left:
                cur.left = node
                return
            elif not cur.right:
                cur.right = node
                return
            else:
                queue.append(cur.left)
                queue.append(cur.right)

    def firstTravel(self,root):
        if root is not None:
            print(root.val)
            self.firstTravel(root.left)
            self.firstTravel(root.right)

    def get_travel(self):
        self.firstTravel(self._root)



if __name__ == '__main__':
    root = None
    tree = Tree(root)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(None)
    tree.add(4)
    tree.get_travel()
