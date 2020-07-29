class Node(object):

    def __init__(self, value: int = 0, side: str = None):
        self.value = value
        self.side  = side
        self.left  = None
        self.right = None


def whitespace(length:int) -> str:
    return ' '*length


class BTree(object):
    def __init__(self):
        self.root = None


    def __insert(self, root: Node, value: int, side: str = None) -> Node:
        if root == None:
            return self.add(value, side)
        else:
            if value <= root.value:
                root.left = self.__insert(root.left, value, 'left')
            else:
                root.right = self.__insert(root.right, value, 'right')
            return root


    def __search(self, root: None, key: int):
        if root == None:
            print('Not found')
        else:
            print(root.value)
            if key == root.value:
                print('This value {} is found in ABB'.format(key))
            elif key < root.value:
                return self.__search(root.left, key)
            elif key > root.value:
                return self.__search(root.right, key)


    def __print(self, root) -> None:
        if not root:
            return

        print(root.value)
        self.__print(root.left)
        self.__print(root.right)


    def __depth(self, root:Node, deep=1) -> int:
        if not root.left and not root.right:
            return deep

        if not root.left:
            return max(self.__depth(root.right, (deep +1)), deep)
        if not root.right:
            return max(self.__depth(root.left, (deep +1)), deep)

        return max(self.__depth(root.left, (deep +1)), self.__depth(root.right, (deep +1)))
    

    def __spacers_print(self, output, offset: int, btwn_space: int) -> None:
        output.append(whitespace(offset))
        output.append('/')
        output.append(whitespace(len(str(btwn_space))))
        output.append('\\')


    def __tree_print(self, output, primary=False, *node) -> None:
        child = []
        edge  = []

        for n in node:
            if not n:
                continue

            if type(n) is int:
                output.append(whitespace(n))
                break

            deep = self.depth(n)
            if primary:
                output.append(whitespace(deep))
                output.append(str(n.value))
                output.append('\n')

                self.__spacers_print(output, deep -1, len(str(n.value)))
                output.append('\n')
                self.__tree_print(output, False, None, n.left, n.right)
                break

            output.append(whitespace(deep))
            output.append(str(n.value))

            if n.left:
                child.append(n.left)
            elif n.right:
                child.append(self.depth(n.right))
            if n.right:
                child.append(n.right)
            elif n.left:
                child.append(self.depth(n.left))

        if child:
            output.append('\n')

            for ch in child:
                if type(ch) is int:
                    continue

                deep = self.depth(ch)
                self.__spacers_print(output, 1, len(str(ch.value)))

            if len(child) > 0:
                output.append('\n')

            self.__tree_print(output, False, *child)


    def add(self, value: int, side: str) -> Node:
        return Node(value, side)


    def insert(self, root: Node, value: int) -> Node:
        return self.__insert(root, value)


    def search(self, root: Node, key: int):
        return self.__search(root, key)


    def print(self, root: Node) -> None:
        return self.__print(root)


    def depth(self, root: Node) -> int:
        return self.__depth(root)


    def tree_print(self, node: Node):
        output = []
        self.__tree_print(output, True, node)
        print(''.join(output))


def generate(btree, start, length):
    from random import randint

    node = btree.insert(None, start)
    for _ in range(length):
        rand = randint(0, length)
        btree.insert(node, rand)
    return node


btree = BTree()

node = btree.insert(None, 10)

btree.insert(node, 9)
btree.insert(node, 12)
btree.insert(node, 11)
btree.insert(node, 8)

# btree.insert(node, 20)
# btree.insert(node, 25)
# node = generate(btree, 7, 8)

# btree.print(node)
# print('-----------')

# print(btree.depth(node))

btree.tree_print(node)
