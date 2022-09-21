import chess.pgn
import networkx as nx

# Load a PGN
pgn = open("pgn-base/lichess-opera-game.pgn")
mygame=chess.pgn.read_game(pgn)
print(mygame.board().fen())

# Create a networkx graph
G=nx.DiGraph()

prev=mygame.board().fen()
G.add_node(prev)
while mygame.next():
    mygame=mygame.next()
    curr=mygame.board().fen()
    G.add_node(curr)
    G.add_edge(prev, curr)
    prev=curr

# create GraphML file
path='gml-base/lichess-opera-game.pgn'
nx.write_gml(G, path)