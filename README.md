Yogisha's Graph Implementation
=========

Usage
--------------
Create a graph.

```sh
g = MyGraph()
```

Add a single edge to the graph. The nodes to be connected, if not already present, are added.

```sh
g.add_edge(2, 3)
```

Add more than one edge at a time:

```sh
g.add_edges([(1,2), (2, 3), (1, 3)])
```

Specify the weight as a fraction between [0, 1]

```sh
g.add_edge(2, 3, 0.5))
g.add_edges([(1, 2, 0.2), (2, 3, 0.8), (1, 3, 0.7)])
```

Find the degree of each node in the graph

```sh
g.degrees()
```

Find the betweenness of each node in the graph

```sh
g.betweenness()
```

Find the closeness of each node in the graph

```sh
g.closeness()
```

Find the shortest distance from a particular node to all other nodes in the graph

```sh
g.dfs(1)
g.bfs(1)
```

Find the shortest path between two particular nodes

```sh
g.shortest_path(1, 2)
```

Find all the connected components in the graph

```sh
g.connected_comps()
```

toygraph:
add return details
start programming

essay:
clean up google doc
write it

contagion:
threshold model
look at data

reus:
give a list of things he could say about me

add/drop forms
update weekly forms
