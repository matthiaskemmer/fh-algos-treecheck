from tree import Tree


def test():
    tree = Tree()
    tree.load_file("data/tree2.txt")
    print("TREECHECK:")
    tree.treecheck(tree.root)
    tree.print_stats()
    print()

    subtree_list = [
        "data/tree2_single_true.txt",
        "data/tree2_single_false.txt",
        "data/tree2_subtree_true.txt",
        "data/tree2_subtree_true2.txt",
        "data/tree2_subtree_true3.txt",
        "data/tree2_subtree_false.txt",
        "data/tree2_subtree_false2.txt",
    ]

    for path in subtree_list:
        print("Searching: ", path)
        tree2 = Tree()
        tree2.load_file(path)
        tree.search(tree2)
        print()


def run():
    file_path = input("Enter tree filepath: ")
    tree = Tree()
    tree.load_file(file_path)
    tree.treecheck(tree.root)
    tree.print_stats()

    file_path2 = input("Enter second tree filepath: ")
    tree2 = Tree()
    tree2.load_file(file_path2)
    tree.search(tree2)


if __name__ == "__main__":
    # run()
    test()
