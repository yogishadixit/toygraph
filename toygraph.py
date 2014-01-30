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
