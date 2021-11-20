# Trees
A tree data structure can be defined recursively as a collection of nodes, where each node is a data structure consisting of a value and a list of references to nodes. The start of the tree is the "root node" and the reference nodes are the "children". No reference is duplicated and none points to the root.

## Challenge
To BinaryTree  that has maximum 2 children and Traverse it using Depth First by preorder, inorder or postorder and to build binary sorted tree that has maximum 2 children to make the searching faster that has two methods (add)   A method that Adds a new node with that value in the correct location in the binary search tree. and (contains) A method that Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
### Binary  tree
#### Traverse
Time complexity:Big O(n)
Space complexity: Big o (n)

### Binary search tree
#### contains and add

Time complexity:BigO(Log N)
Space complexity: Big o (n)


## API
* pre order: traversing path   root >> left >> right
* in order:traversing path     left >> root >> right
* post order:traversing path   left >> right >> root


* Add
 Arguments: value
 Return: nothing
 Adds a new node with that value in the correct location in the binary search tree.

* Contains
 Argument: value
 Returns: boolean indicating whether or not the value is in the tree at least once.


## Structure and Testing
- [x] Can successfully instantiate an empty tree
- [x] Can successfully instantiate a tree with a single root node
- [x] Can successfully add a left child and right child to a  single root node
- [x] Can successfully return a collection from a preorder  traversal
- [x] Can successfully return a collection from an inorder  traversal
- [x] Can successfully return a collection from a postorder traversal
