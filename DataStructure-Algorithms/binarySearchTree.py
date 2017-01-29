#!/usr/bin/python
class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.parent = None
        self.data = key


class Tree:
    root, size = None, 0

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        self.size += 1
        if self.root is None:
            self.root = Node(data)
        else:
            self._insertNode(self.root, data)

    def _insertNode(self, node, data):
        if node.left is None and node.right is None:
            if data > node.data:
                newNode = Node(data)
                node.right = newNode
                newNode.parent = node
            else:
                newNode = Node(data)
                node.left = newNode
                newNode.parent = node
        else:
            if data > node.data:
                if node.right is not None:
                    self._insertNode(node.right, data)
                else:
                    newNode = Node(data)
                    node.right = newNode
                    newNode.parent = node
            else:
                if node.left is not None:
                    self._insertNode(node.left, data)
                else:
                    newNode = Node(data)
                    node.left = newNode
                    newNode.parent = node

    def printTree(self, node):
        if node is None:
            pass
        else:
            self.printTree(node.left)
            print node.data
            self.printTree(node.right)


def main():
    t = Tree()
    t.insert(1)
    t.insert(5)
    t.insert(3)
    t.insert(8)
    t.insert(2)
    t.insert(67)
    t.insert(698)
    t.printTree(t.root)
    

if __name__ == '__main__':
    main()
