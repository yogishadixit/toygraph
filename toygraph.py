from collections import deque

class ToyGraph:
  """A simple implementation of graph manipulation software"""

  def __init__(self):
  	self.nodes = []
  	self.edges = {}

  def add_edge(self, a, b, weight = 1.0):
  	if self.nodes.count(a) == 0:
  	  self.nodes.append(a)
  	  self.edges[a] = []
  	if self.nodes.count(b) == 0:
  	  self.nodes.append(b)
  	  self.edges[b] = []
  	self.edges[a].append((b, weight))
  	self.edges[b].append((a, weight))

  def add_edges(self, x):
    for edge in x:
      if len(edge) == 2:
        self.add_edge(edge[0], edge[1])
      else:
        self.add_edge(edge[0], edge[1], edge[2])

  def degree(self):
    degrees = []
    for node in self.nodes:
      degrees.append((node, len(self.edges[node])))
    return degrees

  def BFS(self, x, y):
    Q = deque()
    V = set()
    Q.append(x)
    V.add(x)
    while (len(Q) != 0):
      t = Q.popleft()
      if t == y:
        return t
      for u,w in self.edges[t]:
        if u not in V:
          V.add(u)
          Q.append(u)
    return None

  def DFS(self, x, y):
    Q = deque()
    V = set()
    Q.append(x)
    V.add(x)
    while (len(Q) != 0):
      t = Q.pop()
      if t == y:
        return t
      for u,w in self.edges[t]:
        if u not in V:
          V.add(u)
          Q.append(u)
    return None

  # uses breadth first search
  def shortest_distances(self, x):
    D = {}
    for node in self.nodes:
      D[node] = -1
    Q = deque()
    Q.append(x)
    D[x] = 0
    while (len(Q) != 0):
      t = Q.popleft()
      for edge in self.edges[t]:
        u = edge[0]
        if (D[u] == -1):
          D[u] = D[t] + edge[1]
          Q.append(u)
    return D

  def shortest_path(self, x, y):
    Prev = {}
    for node in self.nodes:
      Prev[node] = -1
    Q = deque()
    Q.append(x)
    Prev[x] = x
    while (len(Q) != 0):
      t = Q.popleft()
      if y == t:
        path = []
        temp = t
        while (temp != x):
          path.append(temp)
          temp = Prev[temp]
        path.append(x)
        path.reverse()
        return path
      for edge in self.edges[t]:
        u = edge[0]
        if (Prev[u] == -1):
          Prev[u] = t
          Q.append(u)
    return None



  def closeness(self):
    cl = []
    for node in self.nodes:
      sp = self.shortest_distances(node)
      farness = 0
      for e in sp:
        farness = farness + sp[e]
      closeness = 1.0/farness
      cl.append((node, closeness))
    return cl

  def connected_components(self):
    comps = {}
    for node in self.nodes:
      comps[node] = -1
    for node in self.nodes:
      if (comps[node] == -1):
        comps[node] = node
        acc = self.shortest_distances(node)
        for u in acc:
          if (acc[u] != -1):
            comps[u] = node
    return comps
