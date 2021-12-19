from graph import __version__
from graph.graph import Graph
import pytest


def test_bfs_graph():
    graph = Graph()
    v1=graph.add_node(5)
    v2=graph.add_node(7)
    v3=graph.add_node(9)
    graph.add_edge(v1, v2, 1)
    graph.add_edge(v1, v3, 2)
    actual = graph.bfs(v1)
    assert actual == [5, 7, 9]
    assert graph.size() == 3

def test_bfs_with_root_Pandora(bfs):
    graph = bfs[0]
    pandora=bfs[1]
    assert graph.bfs(pandora) == ["Pandora", "Arendelle","Metroville", "Monstroplolis","Narnia","Naboo"]


def test_bfs_with_root_Metroville(bfs):
    graph = bfs[0]
    narnia=bfs[3]
    assert graph.bfs(narnia) ==["Metroville", "Arendelle","Monstroplolis", "Narnia","Naboo","Pandora"]
@pytest.fixture
def bfs():
    graph = Graph()
    v1=graph.add_node("Pandora")
    v2=graph.add_node("Arendelle")
    v3=graph.add_node('Metroville')
    v4=graph.add_node('Monstroplolis')
    v5=graph.add_node('Narnia')
    v6=graph.add_node('Naboo')

    graph.add_edge(v1, v2, 1)
    graph.add_edge(v2, v1, 1)

    graph.add_edge(v2, v3, 1)
    graph.add_edge(v2, v4, 1)
    graph.add_edge(v3, v2, 1)
    graph.add_edge(v4, v2, 1)

    graph.add_edge(v3, v4, 1)
    graph.add_edge(v4, v3, 1)
    graph.add_edge(v3, v5, 1)
    graph.add_edge(v5, v3, 1)
    graph.add_edge(v3, v6, 1)
    graph.add_edge(v6, v3, 1)

    graph.add_edge(v5, v6, 1)
    graph.add_edge(v6, v5, 1)

    graph.add_edge(v6, v4, 1)

    return graph,v1,v2,v3,v4,v5,v6
