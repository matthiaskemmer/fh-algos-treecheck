from node import Node

class Tree:
    """Class representing an AVL tree."""
    
    def __init__(self):
        self.root = None  # root node
        self.stats = None  # tree statistics
        self.is_avl = 'yes' # base case : yes ; if violation -> no

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

        # Update the height of the current node
        curr_node.height = 1 + max(self.get_height(curr_node.left), self.get_height(curr_node.right))
    
        return curr_node

    def get_height(self, node):
        """Get the height of a node in the tree."""
        if not node:
            return 0
        return node.height
    
    def get_balance_factor(self, node_left, node_right):
        height_left = self.get_height(node_left)
        height_right = self.get_height(node_right)
        balance_factor = height_right - height_left
        return balance_factor

    def search(self, value: int):
        """Search whole tree."""
        pass

    def search_subtree(self):
        """Search subtree."""
        pass

    def treecheck(self, node):
        if not node:
            # An empty node is always an AVL node
            return True

        right_subtree_avl = self.treecheck(node.right)
        left_subtree_avl = self.treecheck(node.left)

        # Check if the node's height and balance factor are correct
        height_diff = self.get_height(node.right) - self.get_height(node.left)
        if abs(height_diff) > 1:
            print(f"bal({node.key}) = {height_diff} (AVL violation!)")
            self.is_avl = 'no'
        else:
            print(f"bal({node.key}) = {height_diff}")

        return left_subtree_avl and right_subtree_avl

    def load_file(self, file_path: str):
        """Load tree from text file."""
        with open(file_path, 'r') as file:
            for line in file:
                key = int(line.strip())
                self.add_node(key)

    def update_tree_stats(self, node):
        """Update tree statistics."""
        if not node:
            # An empty node is always an AVL node
            return {'min': None, 'max': None, 'sum': 0, 'count': 0}
        
        right_stats = self.update_tree_stats(node.right)
        left_stats = self.update_tree_stats(node.left)

        # Calculate the min and max values
        min_val = node.key
        max_val = node.key
        if left_stats['min'] is not None:
            min_val = min(left_stats['min'], min_val)
        if right_stats['min'] is not None:
            min_val = min(right_stats['min'], min_val)
        if left_stats['max'] is not None:
            max_val = max(left_stats['max'], max_val)
        if right_stats['max'] is not None:
            max_val = max(right_stats['max'], max_val)
        
        # Calculate the sum and count of all key values
        sum_vals = node.key + left_stats['sum'] + right_stats['sum']
        count = 1 + left_stats['count'] + right_stats['count']

        # Return a dictionary with the min, max, sum, and count
        return {'min': min_val, 'max': max_val, 'sum': sum_vals, 'count': count}

    def print_tree_stats(self):
        """Print out tree statistics."""
        stats = self.update_tree_stats(self.root)
        
        print(f"AVL:", (self.is_avl))
        print(f"min: {stats['min']}, max: {stats['max']}, avg: {stats['sum'] / stats['count']}")


    
    def print_tree_recursive(self, current_node):
        if current_node: #equal to if current_node is None
            self.print_tree_recursive(current_node.left)
            print(current_node.key)
            self.print_tree_recursive(current_node.right)
