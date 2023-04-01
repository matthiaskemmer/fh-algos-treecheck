from node import Node

class Tree:
    """Class representing an AVL tree."""
    
    def __init__(self):
        self.root = None  # root node
        self.stats = None  # tree statistics

    def add_node(self, key: int):
        self.root = self._add_node_recursive(self.root, key)

    def _add_node_recursive(self, curr_node, key):
        if not curr_node:
            return Node(key)

        if key < curr_node.key:
            curr_node.left = self._add_node_recursive(curr_node.left, key)
        elif key > curr_node.key:
            curr_node.right = self._add_node_recursive(curr_node.right, key)
        else:
            # Key already exists in tree, do not insert again
            return curr_node

        # Height of current node
        curr_node.height = 1 + max(self.get_height(curr_node.left), self.get_height(curr_node.right))

        # get balance factor
        balance = self.get_balance_factor(curr_node.left, curr_node.right)

        if balance > 1 and key < curr_node.left.key:
            return self.rotate_right(curr_node)

        if balance < -1 and key > curr_node.right.key:
            return self.rotate_left(curr_node)

        if balance > 1 and key > curr_node.left.key:
            curr_node.left = self.rotate_left(curr_node.left)
            return self.rotate_right(curr_node)

        if balance < -1 and key < curr_node.right.key:
            curr_node.right = self.rotate_right(curr_node.right)
            return self.rotate_left(curr_node)

        return curr_node
    
    def get_height(self, node):
        """Get the height of a node in the tree."""
        if not node:
            return 0
        return node.height
    
    def get_balance_factor(self, node_left, node_right):
        height_left = self.get_height(node_left)
        height_right = self.get_height(node_right)
        balance_factor = height_left - height_right
        return balance_factor

    
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

    def update_tree_stats(self):
        """Update tree statistics."""
        # key min value
        # key max value
        # key arithmetic average
        pass
    
    def _print_tree_recursive(self, current_node):
        if current_node is not None:
            self._print_tree_recursive(current_node.left)
            print(current_node.key)
            self._print_tree_recursive(current_node.right)

            
    def print_tree(self):
        """Print tree nodes in order."""
        self._print_tree_recursive(self.root)