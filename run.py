from tree import Tree

if __name__ == "__main__":
    file_path = input("Enter the path to the tree file: ")
    tree = Tree()
    tree.load_file(file_path)
    #tree.print_tree_recursive(tree.root)
    tree.treecheck(tree.root)
    tree.print_tree_stats()