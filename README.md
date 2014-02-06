Yogisha's Graph Implementation
=========

Usage
--------------
Create a graph.

```sh
> g = MyGraph()
```

Add a single edge to the graph. The nodes to be connected, if not already present, are added.

```sh
> g.add_edge(2, 3)
```

Add more than one edge at a time:

```sh
> g.add_edges([(1,2), (2, 3), (1, 3)])
```

Specify the weight as a fraction between [0, 1]

```sh
> g.add_edge(2, 3, 0.5))
> g.add_edges([(1, 2, 0.2), (2, 3, 0.8), (1, 3, 0.7)])
```

Find the degree of each node in the graph. Output is in the format [(node, in degree, out degree), ...]

```sh
> g.degrees()
[(1, 2, 2), (2, 2, 2), (3, 2, 2)]
```

Find the betweenness of each node in the graph. Output is in the format [(node, betweenness), ...]

```sh
> g.betweenness()
[(1, 1), (2, 0), (3, 0)]
```

Find the closeness of each node in the graph. Output is in the format [(node, closeness), ...]

```sh
> g.closeness()
[(1, .5), (2, .33), (3, .33)]
```

Determines if there is a path from node x to node y. Returns y if such a path exists and None if it does not. 

```sh
> g.dfs(1, 2)
2
> g.bfs(3, 4)
None
```

Find the shortest path between two particular nodes. Returns a list of nodes in which the first element is the start node, the last element is the end node and the elements in between are the shortest traversel necessary to get from the start to the end node.

```sh
> g.shortest_path(1, 2)
[1, 4, 6, 2]
```

Find the shortest distances between the given node and all other nodes. Returns a dictionary of the form { node : distance, ...}

```sh
> g.shortest_distances(1)
{1 : 0, 2 : 1, 3 : 1}
```

Find all the connected components in the graph. Returns a list of toy graph objects, each containing a connected component.

```sh
> g.connected_comps()
TODO: how to show that returning a list of toy graph objects?
```
