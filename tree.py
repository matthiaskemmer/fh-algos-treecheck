import node

class Tree:
    """Class representing an AVL tree."""
    
    def __init__(self):
        self.root = None  # root node
        self.stats = None  # tree statistics

    def add_node(self, node, key: int):
        if not node:
                return node(key)

        if key < node.key:
                node.left = self.add_node(node.left, key)
        elif key > node.key:
                node.right = self.add_node(node.right, key)
        else:
                # Key already exists in tree, do not insert again
                return node

        # Height of current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # get balance factor
        balance = self.get_balance_factor(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
    
    def get_height(self, node):
        """Get the height of a node in the tree."""
        if not node:
            return 0
        return node.height
    
    def get_balance_factor(self, node):
        """Get the balance factor of a node in the tree."""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_left(self, node):
        """Rotate the given node and its right child to the left."""
        right_child = node.right
        left_grandchild = right_child.left

        right_child.left = node
        node.right = left_grandchild

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_child.height = 1 + max(self.get_height(right_child.left), self.get_height(right_child.right))

        return right_child

    def rotate_right(self, node):
        """Rotate the given node and its left child to the right."""
        left_child = node.left
        right_grandchild = left_child.right

        left_child.right = node
        node.left = right_grandchild

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_child.height = 1 + max(self.get_height(left_child.left), self.get_height(left_child.right))

        return left_child

    def search(self, value: int):
        """Search whole tree."""
        pass

    def search_subtree(self):
        """Search subtree."""
        pass

    def treecheck(self):
        """Recursiv tree check."""
        pass

    def load_file(self, file_path: str):
        """Load tree from text file."""
        with open(file_path, 'r') as file:
            for line in file:
                key = int(line.strip())
                self.add_node(key)

    def get_balance_factor(self):
        pass

    def update_tree_stats(self):
        """Update tree statistics."""
        # key min value
        # key max value
        # key arithmetic average
        pass