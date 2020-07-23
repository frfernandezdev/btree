class Node(object):
    value: int  = 0

    def __init__(self, value: int):
        self.value = value
        self.left  = None
        self.right = None


def whitespace(length:int) -> str:
    return ' '*length


class BTree(object):
    def __init__(self):
        self.root = None

    def __insert(self, root: Node, value: int) -> Node:
        if root == None:
            return self.add(value)
        else:
            if value <= root.value:
                root.left = self.__insert(root.left, value)
            else:
                root.right = self.__insert(root.right, value)
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

    def __tree_print(self, output, primary=False, *node) -> None:
        child = []
        edge  = []

        for n in node:
            if not n:
                continue
            
            deep = self.depth(n)
            if primary:
                output.append(whitespace(deep))
                output.append(str(n.value))
                output.append('\n')
                
                output.append(whitespace(deep-1))
                output.append('/')
                output.append('  \\')
                output.append('\n')
                
                self.__tree_print(output, False, n.left, n.right)
                break
            
            output.append(whitespace(deep))
            output.append(str(n.value))
            
            if n.left:
                child.append(n.left)
            if n.right:
                child.append(n.right)

        if child:
            output.append('\n')
            self.__tree_print(output, False, *child)


    def add(self, value: int) -> Node:
        return Node(value)

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
btree.insert(node, 11)
btree.insert(node, 8)
btree.insert(node, 10)
btree.insert(node, 12)
btree.insert(node, 11)
btree.insert(node, 6)
btree.insert(node, 5)
btree.insert(node, 4)
# btree.insert(node, 20)
# btree.insert(node, 25)
# node = generate(btree, 7, 8)

# btree.print(node)
# print('-----------')

# print(btree.depth(node))

btree.tree_print(node)