from graph import __version__
from graph.graph import Graph, Vertex ,Edge
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_empty_graph():
    graph = Graph()
    assert graph

def test_graph_init():
    graph = Graph()
    assert graph._adjacency_list == {}

def test_vertex_init():
    vertex = Vertex("issa")
    assert vertex.value == "issa"

def test_edge_init():
    edge = Edge(401, 2021)
    assert edge.vertex == 401
    assert edge.weight == 2021


def test_vertex_added_to_graph():
    graph = Graph()
    vertex = Vertex(1)
    graph.add_node(vertex)
    assert graph.size() == 1

def test_an_edge_added_to_graph():
    graph = Graph()
    v1=graph.add_node(7)
    v2=graph.add_node(9)
    graph.add_edge(v1, v2, 50)
    vertex_list = graph._adjacency_list[v1]
    edge = vertex_list[0]
    assert edge.vertex == v2
    assert edge.weight == 50

def test_get_nodes():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    assert graph.size() == 2


def test_nodes_in_graph():
    graph = Graph()
    vertex_start = Vertex(1)
    vertex_end = Vertex(2)
    graph.add_node(vertex_start)
    graph.add_node(vertex_end)
    vertex_list = graph.get_nodes()
    assert len(vertex_list) == 2

def test_edges_in_graph():
    graph = Graph()
    v1=graph.add_node(5)
    v2=graph.add_node(7)
    v3=graph.add_node(9)
    graph.add_edge(v1, v2, 1)
    graph.add_edge(v1, v3, 2)
    actual = graph.get_neighbors(v1)
    edge1 = actual[0]
    edge2 = actual[1]
    assert edge1.vertex == v2
    assert edge1.weight == 1
    assert edge2.vertex == v3
    assert edge2.weight == 2
