from binarytrees.Queue import Queue


def breadth_first(tree):
    """
    A function to traverse the tree row by row
    """
    queue=Queue()
    final_output = []

    if  tree.root:
            queue.append(tree.root)
    else:
        return "there is no root "

    while  len(queue):
        front=queue.popleft()
        final_output.append(front.value)

        if front.left :
                queue.append(front.left)
        if front.right :
                queue.append(front.right)
    return final_output

