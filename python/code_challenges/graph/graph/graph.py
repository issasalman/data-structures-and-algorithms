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
  def __init__(self,vertex, weight):
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



# if __name__ == '__main__':
#     graph = Graph()
#     a = graph.add_node('a')
#     b = graph.add_node('b')
#     c = graph.add_node('c')
#     d = graph.add_node('d')
#     e = graph.add_node('e')
#     f = graph.add_node('f')
#     # g = graph.add_node('g')
#     # h = graph.add_node('h')
#     # i = graph.add_node('i')
#     # k = graph.add_node('k')
#     graph.add_edge(a, b)
#     graph.add_edge(a, c)
#     graph.add_edge(a,e)
#     graph.add_edge(b, d)
#     graph.add_edge(c, f)
#     # graph.add_edge(c, b)
#     graph.add_edge(d,e)
#     # graph.add_ed
#     for i in graph.bfs(a):
#       print( i.value)

#     # print((graph.bfs(c)))
