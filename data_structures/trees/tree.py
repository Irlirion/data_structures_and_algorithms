class Node:
    def __init__(self, value: int, parent=None):
        self.value = value
        self.parent = parent
        self.have_child = False
        self.children = []


class SimpleTree:
    def __init__(self, value: int):
        self.root = Node(value)
        self.count_of_nodes = 1

    def add_new_child(self, temp: Node, item: Node):
        temp.children.append(item)
        temp.have_child = True
        if temp == self.root:
            item.parent = self.root
            self.root.have_child = True
        else:
            item.parent = temp
        self.count_of_nodes += 1

    @staticmethod
    def remove_node(node: Node):
        node.parent.children.remove(node)
        if len(node.parent.childs) == 0:
            node.parent.have_child = False
        node.parent = None

    def move_node(self, start: Node, end: Node):
        if start == self.root:
            return
        start.parent.children.remove(start)
        if len(start.parent.children) == 0:
            start.parent.have_child = False
        start.parent = end
        end.have_child = True

    def find_node(self, value: int, node: Node, lst: list) -> Node:
        lst.append(node)
        if node.value == value:
            return node
        for child in node.children:
            n = self.find_node(value, child, lst)
            if n is not None:
                return n
        raise ValueError('Node not found')

    def print_tree(self, node: Node):
        print(node.value, end='\t')
        for child in node.children:
            self.print_tree(child)

    def count_of_lists(self, k: int):
        node = self.root
        if not node.have_child:
            k += 1
        for _ in node.children:
            self.count_of_lists(k)


if __name__ == '__main__':
    tree = SimpleTree(100)
    qqw = []
    a = tree.find_node(100, tree.root, qqw)
    qqw.clear()

    tree.add_new_child(a, Node(99))
    tree.add_new_child(a, Node(0))
    tree.add_new_child(a, Node(1234))

    b = tree.find_node(99, tree.root, qqw)

    qqw.clear()
    tree.add_new_child(b, Node(1050))

    c = tree.find_node(1050, tree.root, qqw)

    tree.add_new_child(c, Node(1))
    tree.print_tree(tree.root)
