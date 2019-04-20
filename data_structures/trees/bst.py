class BinarySearchTree:
    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def get_val(self):
            return self.val

        def set_val(self, new_val):
            self.val = new_val

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def set_left(self, new_left):
            self.left = new_left

        def set_right(self, new_right):
            self.right = new_right

        def __iter__(self):
            if self.left is not None:
                for elem in self.left:
                    yield elem
            yield self.val

            if self.right is not None:
                for elem in self.right:
                    yield elem

    def __init__(self):
        self.root = None

    def insert(self, val):
        def __insert(root, val):
            if root is None:
                return BinarySearchTree.__Node(val)

            if val < root.get_val():
                root.set_left(__insert(root.get_left(), val))
            else:
                root.set_right(__insert(root.get_right(), val))

            return root

        self.root = __insert(self.root, val)

    def __iter__(self):
        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()


def main():
    s = input("Enter a list of numbers: ")
    lst = s.split()

    tree = BinarySearchTree()

    for x in lst:
        tree.insert(float(x))

    for x in tree:
        print(x)
    print()


if __name__ == '__main__':
    main()
