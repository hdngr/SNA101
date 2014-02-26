Build a sample network:

```python
>>>import networkx as nx

>>>G=nx.Graph()
>>>G.add_node(1)
>>>G.add_node(2)
>>>G.add_edge(1,2,foo="bar")

In [17]: G.nodes()
Out[17]: [1, 2]

In [18]: G.edges()
Out[18]: [(1, 2)]

In [19]: G.adj
Out[19]: {1: {2: {'type': 'FRIEND'}}, 2: {1: {'type': 'FRIEND'}}}
```
Build a sample directed network:

```python
>>>G=nx.DiGraph()
>>>G.add_node(1)
>>>G.add_node(2)
>>>G.add_edge(1,2,foo="bar")

In [28]: G.nodes()
Out[28]: [1, 2]

In [27]: G.edges()
Out[27]: [(1, 2)]

In [29]: G.adj
Out[29]: {1: {2: {'somekey': 'LOVERS'}}, 2: {}}
```




