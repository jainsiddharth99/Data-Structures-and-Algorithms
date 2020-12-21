class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class Splay_Tree:

    def __init__(self):
        nil_node = Node(0)
        self.NIL = nil_node
        self.root = self.NIL

    def max(self, x):
        while x.right != self.NIL:
            x = x.right
        return x

    def left_rotation(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:  # x is root
            self.root = y
        elif x == x.parent.left:  # x is left child
            x.parent.left = y
        else:  # x is right child
            x.parent.right = y
        y.left = x
        x.parent = y


def right_rotation(self, x):
    y = x.left
    x.left = y.right
    if y.right != self.NIL:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == self.NIL:  # x is root
        self.root = y
    elif x == x.parent.right:  # x is right child
        x.parent.right = y
    else:  # x is left child
        x.parent.left = y
    y.right = x
    x.parent = y

    def splay(self, n):
        while n.parent != self.NIL:
            if n.parent == self.root:
                if n == n.parent.left:
                    self.right_rotation(n.parent)
                else:
                    self.left_rotation(n.parent)
            else:
                p = n.parent
                g = p.parent

                if n.parent.left == n and p.parent.left == p:
                    self.right_rotation(g)
                    self.right_rotation(p)
                elif n.parent.right == n and p.parent.right == p:
                    self.left_rotation(g)
                    self.left_rotation(p)
                elif n.parent.right == n and p.parent.left == p:
                    self.left_rotation(p)
                    self.right_rotation(g)
                elif n.parent.left == n and p.parent.right == p:
                    self.right_rotation(p)
                    self.left_rotation(g)

    def insertion(self, n):

        y = self.NIL
        temp = self.root

        while temp != self.NIL:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        n.parent = y

        if y == self.NIL:
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n

        self.splay(n)

    def search(self, n, x):

        if x == n.data:
            self.splay(n)
            return n
        elif x < n.data:
            return self.search(n.left, x)
        elif x > n.data:
            return self.search(n.right, x)
        else:
            return self.NIL

    def delete(self, n):

        self.splay(n)

        left_subtree = SplayTree()
        left_subtree.root = self.root.left

        if left_subtree.root != self.NIL:
            left_subtree.root.parent = self.NIL

        right_subtree = SplayTree()
        right_subtree.root = self.root.right

        if right_subtree.root != self.NIL:
            right_subtree.root.parent = self.NIL

        if left_subtree.root != self.NIL:
            m = left_subtree.maximum(left_subtree.root)
            left_subtree.splay(m)
            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root
        else:
            self.root = right_subtree.root

    def preorder(self, n):

        if n != self.NIL:
            print(n.data)
            self.preorder(n.left)
            self.preorder(n.right)


if __name__ == '__main__':
    ft = Splay_Tree()

    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(100)
    e = Node(90)
    f = Node(40)
    g = Node(50)
    h = Node(60)
    i = Node(70)
    j = Node(80)
    k = Node(150)
    l = Node(110)
    m = Node(120)
    n = Node(45)
    o = Node(55)
    p = Node(65)
    r = Node(750)
    s = Node(25)
    t = Node(130)

    ft.insertion(a)
    ft.insertion(b)
    ft.insertion(c)
    ft.insertion(d)
    ft.insertion(e)
    ft.insertion(f)
    ft.insertion(g)
    ft.insertion(h)
    ft.insertion(i)
    ft.insertion(j)
    ft.insertion(k)
    ft.insertion(l)
    ft.insertion(m)
    ft.insertion(n)
    ft.insertion(o)
    ft.insertion(p)
    ft.insertion(r)
    ft.insertion(r)
    ft.insertion(s)
    ft.insertion(t)

    ft.delete(a)
    ft.delete(m)
    ft.delete(t)
    ft.delete(r)

    ft.preorder(ft.root)