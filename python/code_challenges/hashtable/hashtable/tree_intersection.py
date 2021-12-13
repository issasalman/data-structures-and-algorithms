from hashtable.hashtable import HashTable
from hashtable.binary_tree import BinaryTree,Node

def tree_intersection(Tree1,Tree2):
    nodes_intersection = []
    hashed = HashTable()
    tree1 = Tree1.in_order()
    tree2 = Tree2.in_order()
    if not tree1 or not tree2:
        return []
    for node in tree1:
        hashed.add(node,node)
    for node in tree2:
        if hashed.contains(node):
            nodes_intersection.append(node)
        hashed.add(node,node)
    if len(nodes_intersection)==0:
        return "no repeat"
    return nodes_intersection

if __name__ == '__main__':
    
    tree1 = BinaryTree()
    tree1.root=Node(1,Node(4,Node(3),Node(55)),Node(2,Node(3)))

    tree2 = BinaryTree()
    tree2.root=Node(4,Node(4,Node(3),Node(55)),Node(2,Node(32)))


    print(tree_intersection(tree1,tree2))
