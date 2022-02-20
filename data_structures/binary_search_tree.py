class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:

    def insert(self, node, value):
        if node is None:
            return Node(value)
        else:
            if value < node.value:
                node.left = self.insert(node.left, value)
            else:
                node.right = self.insert(node.right, value)
            return node

    def search(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        else:
            if value < node.value:
                self.search(node.left, value)
            else:
                self.search(node.right, value)

    def get_minimum_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, value):

        if root is None:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)

        elif value > root.value:
            root.right = self.delete(root.right, value)

        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_minimum_node(root.right)
            root.value = temp.value

            root.right = self.delete(root.right, temp.value)

        return root

    def print_in_order(self, node):
        if node is not None:
            self.print_in_order(node.left)
            print(node.value, end=" ")
            self.print_in_order(node.right)

    def print_pre_order(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.print_in_order(node.left)
            self.print_in_order(node.right)

    def print_post_order(self, node):
        if node is not None:
            self.print_in_order(node.left)
            self.print_in_order(node.right)
            print(node.value, end=" ")


if __name__ == '__main__':

    values = [3, 6, 33, 7, 7, 5, 12, 57, 98, 234, 2]

    tree = Tree()
    root = tree.insert(node=None, value=values[0])

    for i in range(1, len(values)):
        tree.insert(root, values[i])

    tree.print_in_order(root)

    # print('found') if tree.search(12) is not None else print('not found')
    # print('found') if tree.search(97) is not None else print('not found')
    # print('found') if tree.search(3) is not None else print('not found')
    # print('found') if tree.search(124) is not None else print('not found')
    # print('found') if tree.search(4) is not None else print('not found')
    print('\n')
    tree.delete(root, 98)
    tree.print_in_order(root)

    print('\n')
    tree.delete(root, 33)
    tree.print_in_order(root)

    print('\n')
    tree.delete(root, 2)
    tree.print_in_order(root)

    print('\n')
    tree.delete(root, 12)
    tree.print_in_order(root)

    print('\n')
    tree.delete(root, 5)
    tree.print_in_order(root)

    print('\n')
    tree.delete(root, 3)
    tree.print_in_order(root)

    # print('\n')
    # tree.delete(root, 3)
    # tree.print_in_order(root)

    # print('\n')
    # tree.delete(root, 7)
    # tree.print_in_order(root)

    # print('\n')
    # tree.delete(root, 7)
    # tree.print_in_order(root)

