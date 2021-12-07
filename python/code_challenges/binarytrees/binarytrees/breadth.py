from binarytrees.Queue import Queue


def breadth_first(tree):
    """
    A function to traverse the tree row by row
    """
    queue=Queue()
    final_output = []

    if  tree.root:
            queue.enqueue(tree.root)
    else:
        return "there is no root "

    while not queue.is_empty():
        front=queue.dequeue()
        final_output.append(front.value)

        if front.left :
                queue.enqueue(front.left)
        if front.right :
                queue.enqueue(front.right)
    return final_output

