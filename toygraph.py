fron collections import deque

class ToyGraph:
  """A simple implementation of graph manipulation software"""

  def __init__(self):
  	self.nodes = []
  	self.edges = {}

  def add_edge(a, b, weight = 1.0):
  	if nodes.count(a) == 0:
  	  nodes.append(a)
  	  edges[a] = []
  	if nodes.count(b) == 0:
  	  nodes.append(b)
  	  edges[b] = []
  	edges[a].append(b, weight)
  	edges[b].append(a, weight)

  def add_edges(x):
  	for edge in x:
  	  add_edge(edge)

  def degree():
    degrees = []
    for node in nodes:
      degrees.append((node, len(edges[node])))
    return degrees

  def BFS(x, y):
    Q = deque()
    V = set()
    Q.append(x)
    V.update(x)
    while !Q:
      t = Q.popleft()
      if t == y:
        return t
      for u in edges[t]:
        if u not in V:
          V.update(u)
          Q.append(u)
    return None

  def DFS(x, y):
    S = []
    V = set()
    Q.append(x)
    V.update(x)
    while !Q.empty():
      t = Q.pop()
      if t == y:
        return t
      for u in edges[t]:
        if u not in V:
          V.update(u)
          Q.append(u)
    return None

  # uses breadth first search
  def shortest_distances(x):
    D = {}
    for node in nodes:
      D[node] = -1
    Q = deque()
    Q.append(x)
    D[x] = 0
    while !Q:
      t = Q.popleft()
      for edge in edges[t]:
        u = edge[0]
        if D[u] = -1:
          D[u] = D[t] + edge[1]
          Q.append(u)
    return D

  def shortest_path(x, y):
    Prev = {}
    for node in nodes:
      Prev[node] = -1
    Q = deque()
    Q.append(x)
    Prev[x] = x
    while !Q:
      t = Q.popleft()
      if y == t:
        path = []
        #TODO: print shortest path
        return path
      for edge in edges[t]:
        u = edge[0]
        if Prev[u] = -1:
          Prev[u] = t
          Q.append(u)
    return None



  def closeness():
    cl = []
    for node in nodes:
      sp = shortest_distances(node)
      farness = 0
      for e in sp:
        farness = farness + sp[e]
      closeness = 1.0/farness
      cl.append((node, closeness))
    return cl
