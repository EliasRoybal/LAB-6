import time
from LAB6B import *


def main():
    print("Graphs created using Kruskal's algorithm")
    print()
    # Tests for Kruskal's algorithm
    start_time1 = int(round(time.time() * 1000))
    g = KruskalGraph(4)
    g.add_edge(1, 3, 15)
    g.add_edge(0, 1, 8)
    g.add_edge(2, 1, 12)

    g.kruskal()
    print("Running time for test 1: %s milliseconds " % (start_time1 - time.time()))
    print("")

    start_time2 = int(round(time.time() * 1000))
    g = KruskalGraph(4)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 9)
    g.add_edge(2, 0, 13)
    g.add_edge(3, 1, 4)
    g.add_edge(1, 2, 12)
    g.add_edge(1, 0, 111)

    g.kruskal()
    print("Running time for test 2: %s milliseconds " % (start_time2 - time.time()))
    print("")

    # Tests for topological sorting
    start_time3 = int(round(time.time() * 1000))
    g = TopologicalGraph()

    vertex1 = Vertex('70')
    vertex2 = Vertex('71')
    vertex3 = Vertex('22')
    vertex4 = Vertex('1')
    vertex5 = Vertex('0')
    vertex6 = Vertex('9')
    vertex7 = Vertex('14')

    g.add_vertex(vertex1)
    g.add_vertex(vertex2)
    g.add_vertex(vertex3)
    g.add_vertex(vertex4)
    g.add_vertex(vertex5)
    g.add_vertex(vertex6)
    g.add_vertex(vertex7)

    g.add_directed_edge(vertex1, vertex2)
    g.add_directed_edge(vertex1, vertex3)
    g.add_directed_edge(vertex2, vertex6)
    g.add_directed_edge(vertex3, vertex4)
    g.add_directed_edge(vertex4, vertex6)
    g.add_directed_edge(vertex5, vertex6)
    g.add_directed_edge(vertex5, vertex7)
    g.add_directed_edge(vertex6, vertex7)

    # do topological sort on the graph
    print("Graphs created with topological sorting")
    print("")
    result_list = topological_sort(g)

    # display sorted list
    first = True
    for vertex in result_list:
        if first:
            first = False
        else:
            print(' -> ', end='')
        print(vertex.label, end='')
    print()
    print("Running time for test 1: %s milliseconds " % (start_time3 - time.time()))
    print("")
    start_time4 = int(round(time.time() * 1000))
    g = TopologicalGraph()

    vertex11 = Vertex('5')
    vertex22 = Vertex('19')
    vertex33 = Vertex('77')
    vertex44 = Vertex('38')
    vertex55 = Vertex('15')
    vertex66 = Vertex('49')
    vertex77 = Vertex('97')

    g.add_vertex(vertex11)
    g.add_vertex(vertex22)
    g.add_vertex(vertex33)
    g.add_vertex(vertex44)
    g.add_vertex(vertex55)
    g.add_vertex(vertex66)
    g.add_vertex(vertex77)

    g.add_directed_edge(vertex55, vertex77)
    g.add_directed_edge(vertex22, vertex33)
    g.add_directed_edge(vertex11, vertex77)
    g.add_directed_edge(vertex33, vertex33)
    g.add_directed_edge(vertex77, vertex66)
    g.add_directed_edge(vertex55, vertex66)
    g.add_directed_edge(vertex44, vertex11)
    g.add_directed_edge(vertex22, vertex44)

    result_list = topological_sort(g)

    # display sorted list
    first = True
    for vertex in result_list:
        if first:
            first = False
        else:
            print(' -> ', end='')
        print(vertex.label, end='')
    print()
    print("Running time for test 2: %s milliseconds " % (start_time4 - time.time()))


main()
