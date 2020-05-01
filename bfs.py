class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BTree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, val):
        self._root = val

    def insert_node(self, node: int):  # BFS
        # if self.root is None:
        #     self.root = TreeNode(node)
        #     return
        q = [self.root]
        while q:
            cur = q.pop(0)
            if cur is None:
                self.root = TreeNode(node) if node is not None else None
                return
            if cur.left is None:
                cur.left = TreeNode(node) if node is not None else None
                return
            if cur.right is None:
                cur.right = TreeNode(node) if node is not None else None
                return
            else:
                q.append(cur.left)
                q.append(cur.right)

    def insert_list_data(self, data_list: list):
        for i in data_list:
            self.insert_node(i)

    def first_travel(self, root):
        """先序遍历"""
        if root is not None:
            print(root.val)
            self.first_travel(root.left)
            self.first_travel(root.right)

    def get_first_travel(self):
        self.first_travel(self.root)

    def get_min_depth(self):
        q = [self.root]
        depth = 1
        while q:
            q_size = len(q)
            i = 0
            while i < q_size:
                cur = q.pop(0)
                if cur.left is None and cur.right is None:
                    return depth
                q.append(cur.left)
                q.append(cur.right)
                i += 1
            depth += 1


def openLock(deadends: list, target: str) -> int:
    def plusOne(cur: tuple, j):
        cur = list(cur)
        if cur[j] == 9:
            cur[j] = 0
            return tuple(cur)
        cur[j] += 1
        return tuple(cur)
    def minusOne(cur:tuple, j):
        cur = list(cur)
        if cur[j] == 0:
            cur[j] = 9
            return tuple(cur)
        else:
            cur[j] -= 1
            return tuple(cur)

    q1, q2 = {(0,0,0,0)},{tuple(map(int,target))}
    time = 0
    visited, dead_end = set(),set(tuple(map(int,i)) for i in deadends)
    while q1 and q2:
        if len(q2) < len(q1):
            q1, q2 = q2, q1
        new_q = set()
        for i in q1:
            visited.add(i)
            if i in q2:
                return time
            elif i not in dead_end:
                for j in range(0,4):
                    tmp = plusOne(i, j)
                    if tmp not in visited:
                        new_q.add(tmp)
                    down = minusOne(i, j)
                    if down not in visited:
                        new_q.add(down)
        q1,q2 = q2, new_q
        time += 1
    return -1


if __name__ == '__main__':
    print(openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
    # a = BTree()
    # a.insert_list_data([3, 9, 20, None, None, 15, 7])
    # #a.get_first_travel()
    # print(a.get_min_depth())
