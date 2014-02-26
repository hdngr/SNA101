# -*- coding: utf-8 -*-
# Girvan Newman algorithmを使って空手クラブネットワークのコミュニティが分割していく様子を出力
# Zachary's karate club(空手クラブのネットワーク)のデータ取得元URL
# http://www-personal.umich.edu/~mejn/netdata/

import networkx as NX
import networkx.algorithms.centrality as NC
import pylab as P


def updateGraph(G):
    ebc = NC.edge_betweenness(G)
    maxs = 0
    medge = None
    for k, v in ebc.iteritems():
        if maxs < v:
            medge, maxs = k, v
    G.remove_edge(*medge)


def drawGraph(G, pos, output):
    NX.draw(G, pos)
    P.savefig(output)
    P.draw()
    P.close()

G = NX.karate_club_graph()
eNum = G.number_of_edges()
pos = NX.spring_layout(G)
for i in range(eNum):
    import pdb; pdb.set_trace()
    pos = NX.spring_layout(G)
    output = "img/karate%(id)02d.png" % {"id": i}
    drawGraph(G, pos, output)
    updateGraph(G)