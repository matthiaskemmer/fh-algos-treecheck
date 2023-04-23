# Task 2 TREECHECK - Algorithmen und Datenstrukturen (ALGOS)

Group project for second semester course "Algorithmen und Datenstrukturen" (ALGOS) at FH Technikum Wien.

Authors: Matthias Kemmer, Li Wen Wang

## Task
The task was to create a programm to built binary trees from text files and check if those trees are balanced AVL trees or not. It is possible to calculare and print the balance factor for each node as well as tree statistics. The tree can also be searched for a single value or a subtree.

## Input format
Example file: `tree.txt`
```
5
3
17
9
23
54
11
79
30
12
```

## Output
Example output (AVL check and tree statistics) for `tree.txt`
```
bal(79) = 0
bal(30) = 0
bal(54) = 0
bal(23) = 2 (AVL violation!)
bal(12) = 0
bal(11) = 1
bal(9) = 2 (AVL violation!)
bal(17) = 0
bal(3) = 0
bal(5) = 3 (AVL violation!)
AVL: no
min: 3, max: 79, avg: 24.3
```
