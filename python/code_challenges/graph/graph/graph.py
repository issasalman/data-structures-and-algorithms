from collections import deque


class Queue:
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.append(value)

  def dequeue(self):
    return self.dq.popleft()

  def __len__(self):
    return len(self.dq)

class Stack:
    def __init__(self):
        self.dq = deque()

    def push(self, value):
        self.dq.append(value)

    def pop(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)




class Vertex:
    """
    Input:Value
    qualifier: Store the value
    Return: None
    """

    def __init__(self, value=None):
        self.value = value


class Edge:
    """
    Input: Vertex, weight
    qualifier: Store the vertex and the weight
    Return: None
    """

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    """
    Input: None
    qualifier: It is initializing  an empty graph
    Return: None
    """

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """
         Input : Value
         qualifier : add a node to the Graph
         Return : node
        """
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Input: start_vertex, end_vertex , weight:optional
        qualifier: Creates an edge and append that edge to the value of
        start_vertex inside the _adjacency_list
        Return: None
        """

        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex is not found")
        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex is not found")
        edge = Edge(end_vertex, weight)
        self._adjacency_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        """
        Input : Vertex
        qualifier: Get all neighbors for a vertex
        Return: a list of edges
        """
        return self._adjacency_list.get(vertex, [])

    def get_nodes(self):
        """
        Input : None
        qualifier : get all the nodes in the graph as a set or list
        Return : a list or set of the nodes
        """
        return self._adjacency_list.keys()

    def size(self):
        """
        Input: None
        qualifier: find the length of the _adjacency_list
        Return: int The size(the length of _adjacency_list)
        """
        return len(self._adjacency_list)


    def bfs(self, start_vertex):

        queue = Queue()
        result = []
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        result.append(start_vertex.value)

        while len(queue):
            current_vertex = queue.dequeue()

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
                    result.append(neighbor.value)

        return result

    def dfs(self, start_vertex):
        """
        Perform a depth first search on the graph in pre order traversal
        Arguments: start_vertex
        Returns: collection of nodes
        """
        stack = Stack()
        pre_output = []
        visited = set()

        stack.push(start_vertex)
        visited.add(start_vertex)


        while stack:
            current_vertex = stack.pop()


            pre_output.append(current_vertex.value)
            neighbors = self.get_neighbors(current_vertex)
            for edge in neighbors :
                neighbor = edge.vertex
                if edge.vertex not in visited:
                    visited.add(neighbor)
                    stack.push(neighbor)

        return pre_output

if __name__ == '__main__':
    graph = Graph()
    Pandora=graph.add_node("Pandora")
    Arendelle=graph.add_node("Arendelle")
    Metroville=graph.add_node('Metroville')
    Monstroplolis=graph.add_node('Monstroplolis')
    Narnia=graph.add_node('Narnia')
    Naboo=graph.add_node('Naboo')

    graph.add_edge(Pandora, Arendelle, 150)
    graph.add_edge(Arendelle, Pandora, 150)

    graph.add_edge(Arendelle, Metroville, 99)
    graph.add_edge(Arendelle, Monstroplolis, 42)
    graph.add_edge(Metroville, Arendelle, 99)
    graph.add_edge(Monstroplolis, Arendelle,42)

    graph.add_edge(Metroville, Monstroplolis, 105)
    graph.add_edge(Monstroplolis, Metroville, 105)
    graph.add_edge(Metroville, Narnia, 37)
    graph.add_edge(Narnia, Metroville,37)
    graph.add_edge(Metroville, Naboo, 26)
    graph.add_edge(Metroville, Pandora, 82)
    graph.add_edge(Pandora, Metroville, 82)


    graph.add_edge(Naboo, Metroville, 26)

    graph.add_edge(Narnia, Naboo, 250)
    graph.add_edge(Naboo, Narnia, 250)

    graph.add_edge(Naboo, Monstroplolis, 73)
    graph.add_edge(Monstroplolis, Naboo, 73)

    for i in graph.dfs(Pandora):
      print( i)

    # print((graph.bfs(c)))
