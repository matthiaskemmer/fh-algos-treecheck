class Node:
    """Class representing a node in a tree."""
    
    def __init__(self, key: int, right=None, left=None):
        self.key = key
        self.right = right
        self.left = left
        self.height = 1