from graph import __version__
from graph.graph import Graph
import pytest


def test_dfs_graph():
    graph = Graph()
    v1=graph.add_node(5)
    v2=graph.add_node(7)
    v3=graph.add_node(9)
    graph.add_edge(v1, v2, 1)
    graph.add_edge(v1, v3, 2)
    actual = graph.dfs(v1)
    assert actual == [5, 9, 7]
    assert graph.size() == 3

def test_dfs_with_root_Pandora(dfs):
    graph = dfs[0]
    pandora=dfs[1]
    assert graph.dfs(pandora) == ['Pandora', 'Metroville', 'Naboo', 'Narnia', 'Monstroplolis', 'Arendelle']


def test_dfs_with_root_Metroville(dfs):
    graph = dfs[0]
    narnia=dfs[3]
    assert graph.dfs(narnia) ==['Metroville', 'Pandora', 'Naboo', 'Narnia', 'Monstroplolis', 'Arendelle']

@pytest.fixture
def dfs():
    graph = Graph()
    Pandora=graph.add_node("Pandora")
    Arendelle=graph.add_node("Arendelle")
    Metroville=graph.add_node('Metroville')
    Monstroplolis=graph.add_node('Monstroplolis')
    Narnia=graph.add_node('Narnia')
    Naboo=graph.add_node('Naboo')

    graph.add_edge(Pandora, Arendelle,150)
    graph.add_edge(Arendelle, Pandora,150)

    graph.add_edge(Arendelle, Metroville,99)
    graph.add_edge(Arendelle, Monstroplolis,42)
    graph.add_edge(Metroville, Arendelle,99)
    graph.add_edge(Monstroplolis, Arendelle,42)

    graph.add_edge(Metroville, Monstroplolis,105)
    graph.add_edge(Monstroplolis, Metroville,105)
    graph.add_edge(Metroville, Narnia,37)
    graph.add_edge(Narnia, Metroville,37)
    graph.add_edge(Metroville, Naboo,26)
    graph.add_edge(Metroville, Pandora,82)
    graph.add_edge(Pandora, Metroville,82)


    graph.add_edge(Naboo, Metroville,26)

    graph.add_edge(Narnia, Naboo,250)
    graph.add_edge(Naboo, Narnia,250)

    graph.add_edge(Naboo, Monstroplolis,73)
    graph.add_edge(Monstroplolis, Naboo,73)


    return graph,Pandora,Arendelle,Metroville,Monstroplolis,Narnia,Naboo

