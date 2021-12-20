from graph import Graph

def business_trip(graph, arr_city):
    """
    Write a function called business trip
    What does it do : Determine whether the trip is possible with direct flights, and how much it would cost.
    Arguments: graph, array of city names
    Return: cost or null
    """
    trip = False
    cost = 0

    for i in range(len(arr_city) - 1):
        neighbors = graph._adjacency_list[arr_city[i]]
        # print(neighbors[0].vertex.value)
        # print(neighbors[1].vertex.value)
        # print(neighbors[2].vertex.value)

        trip = False

        for neighbor in neighbors:

            if neighbor.vertex ==arr_city[i + 1]:
                trip = True
                cost += neighbor.weight

    if not trip:
        cost = 0
        trip = False
        return f"{trip},${cost}"

    return f"{trip},${cost}"

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


    print(business_trip(graph,[Pandora,Metroville,Arendelle]))
