# src/graph_adjlist.py
from collections import defaultdict,deque
buildings={1:"Library",2:"Admin",3:"Hostel",4:"CSE",5:"Cafe"}
edges=[(1,2,50),(1,3,120),(2,4,70),(3,5,60),(4,5,40)]

def build_adjlist(edges):
    g=defaultdict(list)
    for u,v,w in edges:
        g[u].append((v,w)); g[v].append((u,w))
    return g

def bfs(s,g):
    vis={s}; q=deque([s]); order=[]
    while q:
        u=q.popleft(); order.append(u)
        for v,_ in g[u]:
            if v not in vis: vis.add(v); q.append(v)
    return order

def demo_graph():
    g=build_adjlist(edges)
    print("Adjacency list:", dict(g))
    print("BFS from 1:", bfs(1,g))
