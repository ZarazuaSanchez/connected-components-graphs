from connected_components_graphs import *
from graphs import *

exGraph = UndirectedGraph({'a', 'b'}, {'a', 'c'},
                          {'b', 'c'}, {'b', 'd'},
                          {'e', 'f'}, {'e', 'g'},
                          {'h', 'i'})
exGraph.addVertices('j') #add lone vertex

if __name__ == '__main__':

    djsets = findConnectedComps(exGraph)

    print('example G in set notation G = (E, V)\n')
    print('Vertices: {}'.format(exGraph.vertices))
    print()
    print('Edges: {}\n'.format(exGraph.edges))

    print('Sets of Connected Components:')
    for rep, restofset in djsets.items():
        print("{}: {}".format(rep, restofset))
