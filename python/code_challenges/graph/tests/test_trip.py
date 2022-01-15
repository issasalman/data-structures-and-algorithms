from graph import __version__
from graph.graph import Graph
from  graph.trip import business_trip
import pytest

def test_business_trip1(bt):
    array=[bt[1],bt[2]]
    expected=business_trip(bt[0],array)
    actual="True,$150"
    assert actual == expected

def test_business_trip2(bt):
    array=[bt[1],bt[2],bt[3]]
    expected=business_trip(bt[0],array)
    actual="True,$249"
    assert actual == expected

def test_business_trip3(bt):
    array=[bt[1],bt[2],bt[5]]
    expected=business_trip(bt[0],array)
    actual="False,$0"
    assert actual == expected



@pytest.fixture
def bt():
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

