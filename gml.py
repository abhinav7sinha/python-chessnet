import os
os.system('cls' if os.name == 'nt' else 'clear')

import chess.pgn
import networkx as nx

class GraphMLUtil:
    def loadSinglePgnFile(self, path):
        '''
        takes path of pgn file as input
        loads python-chess game object in self.singleGame
        '''
        singlePgn = open("pgn-base/lichess-opera-game.pgn")
        self.singleGame = chess.pgn.read_game(singlePgn)
        
        # extract file name of the pgn file -> to be used as the file name for the generated gml file
        self.pgnFileName=os.path.splitext(os.path.basename(path))[0]

    def generateGameGml(self, graphType='DiGraph', dest='gml-base'):
        '''
        generates graphML file and saves it in dest folder with name self.pgnFileName
        '''
        if graphType=='DiGraph':
            diGraph=nx.DiGraph()
            game=self.singleGame
            prev=game.board().fen()
            diGraph.add_node(prev)
            while game.next():
                game=game.next()
                curr=game.board().fen()
                diGraph.add_node(curr)
                diGraph.add_edge(prev, curr)
                prev=curr

            # create GraphML file
            if dest=='gml-base':
                # if dest is not specified -> store gml file in default dir with default filename
                path=os.path.join(dest, self.pgnFileName+'.gml')
                nx.write_gml(diGraph, path)
            else:
                nx.write_gml(diGraph, dest)