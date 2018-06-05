# Implementation of Binary SearchTree


class Node(object):
    def __init__(self, data):
        self.data = data
        self.l_link = None
        self.r_link = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, root, new_node):
        if root is None:
            root = new_node
        else:
            if root.data >= new_node.data:
                if root.l_link is None:
                    root.l_link = new_node
                else:
                    self.insert(root.l_link, new_node)
            if root.data < new_node.data:
                if root.r_link is None:
                    root.r_link = new_node
                else:
                    self.insert(root.r_link, new_node)

    def in_order(self, root):
        if root:
            self.in_order(root.l_link)
            print(root.data, end=" ")
            self.in_order(root.r_link)

    def pre_order(self, root):
        if root:
            print(root.data, end=" ")
            self.pre_order(root.l_link)
            self.pre_order(root.r_link)

    def post_order(self, root):
        if root:
            print(root.data, end=" ")
            self.post_order(root.r_link)
            self.post_order(root.l_link)


if __name__ == '__main__':
    binarySearchTree = BinarySearchTree()
    root = Node(15)

    binarySearchTree.insert(root, Node(10))
    binarySearchTree.insert(root, Node(20))
    binarySearchTree.insert(root, Node(8))
    binarySearchTree.insert(root, Node(12))
    binarySearchTree.insert(root, Node(17))
    binarySearchTree.insert(root, Node(25))

    binarySearchTree.pre_order(root)
    print(end="\n")
    binarySearchTree.in_order(root)
    print(end="\n")
    binarySearchTree.post_order(root)
