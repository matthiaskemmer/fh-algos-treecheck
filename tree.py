from node import Node


class Tree:
    """Class representing an AVL tree."""

    def __init__(self):
        self.root = None
        self.stats = None
        self.is_avl = True  # is tree valid avl tree
        self.val_found = False  # is searched value in tree
        self.search_path = list()  # path from root to searched value
        self.subtree_root = None # set the root for subtree search

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
        curr_node.height = 1 + max(
            self.get_height(curr_node.left), self.get_height(curr_node.right)
        )

        return curr_node

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance_factor(self, node_left, node_right):
        height_left = self.get_height(node_left)
        height_right = self.get_height(node_right)
        balance_factor = height_right - height_left
        return balance_factor

    def get_node(self, curr_node, val):
        if not curr_node:
            return

        if val == curr_node.key:
            self.subtree_root = curr_node

        if val < curr_node.key and curr_node.left:
            self.get_node(curr_node.left, val)

        if val > curr_node.key and curr_node.right:
            self.get_node(curr_node.right, val)

    def search(self, other):
        subtree_search = True if (other.root.left or other.root.right) else False

        if subtree_search:
            nodes = list()
            self.get_subtree_nodes(other.root, nodes)
            self.get_node(self.root, other.root.key)
            if self.subtree_root and all(
                [self.search_single(self.subtree_root, val) for val in nodes]
            ):
                print("Subtree found")
            else:
                print("Subtree not found")
        else:
            # Single value search
            found = self.search_single(self.root, other.root.key)
            if found:
                path = [str(x) for x in self.search_path]
                print(f"{other.root.key} found " + ", ".join(path))
            else:
                print(f"{other.root.key} not found")

    def search_single(self, root, val):
        self.val_found = False
        self.search_path = list()
        self.search_value(root, val)
        return self.val_found

    def search_value(self, curr_node, val):
        if not curr_node:
            self.val_found = False
            return

        self.search_path.append(curr_node.key)

        if val == curr_node.key:
            self.val_found = True
            return

        if val < curr_node.key and curr_node.left:
            self.search_value(curr_node.left, val)

        if val > curr_node.key and curr_node.right:
            self.search_value(curr_node.right, val)

    def get_subtree_nodes(self, node, nodes):
        if node:
            self.get_subtree_nodes(node.right, nodes)
            self.get_subtree_nodes(node.left, nodes)
            nodes.append(node.key)

    def treecheck(self, node):
        if not node:
            # An empty node is always an AVL node
            return True

        self.treecheck(node.right)
        self.treecheck(node.left)

        # Check if the node's height and balance factor are correct
        height_diff = self.get_height(node.right) - self.get_height(node.left)
        if abs(height_diff) > 1:
            print(f"bal({node.key}) = {height_diff} (AVL violation!)")
            self.is_avl = False
        else:
            print(f"bal({node.key}) = {height_diff}")

    def load_file(self, file_path: str):
        with open(file_path, "r") as file:
            for line in file:
                key = int(line.strip())
                self.add_node(key)

    def update_stats(self, node):
        if not node:
            # An empty node is always an AVL node
            return {"min": None, "max": None, "sum": 0, "count": 0}

        right_stats = self.update_stats(node.right)
        left_stats = self.update_stats(node.left)

        # Calculate the min and max values
        min_val = node.key
        max_val = node.key
        if left_stats["min"]:
            min_val = min(left_stats["min"], min_val)
        if right_stats["min"]:
            min_val = min(right_stats["min"], min_val)
        if left_stats["max"]:
            max_val = max(left_stats["max"], max_val)
        if right_stats["max"]:
            max_val = max(right_stats["max"], max_val)

        # Calculate the sum and count of all key values
        sum_vals = node.key + left_stats["sum"] + right_stats["sum"]
        count = 1 + left_stats["count"] + right_stats["count"]

        # Return a dictionary with the min, max, sum, and count
        return {"min": min_val, "max": max_val, "sum": sum_vals, "count": count}

    def print_stats(self):
        stats = self.update_stats(self.root)

        print(f"AVL:", "yes" if self.is_avl else "no")
        print(
            f"min: {stats['min']}, max: {stats['max']}, avg: {stats['sum'] / stats['count']}"
        )

    def print_tree(self, current_node):
        if current_node:
            self.print_tree(current_node.left)
            print(current_node.key)
            self.print_tree(current_node.right)
