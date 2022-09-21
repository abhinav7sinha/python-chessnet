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
        singlePgn = open(path)
        self.singleGame = chess.pgn.read_game(singlePgn)
        
        # extract file name of the pgn file -> to be used as the file name for the generated gml file
        self.pgnFileName=os.path.splitext(os.path.basename(path))[0]

    def generateGamesNetwork(self, path):
        '''
        Takes path of pgn file as input.
        Loops through all the games in the PGN:
            - iteratively creating FENs for each of the position in these game
            - and creates networkx graph objects with FENs as nodes
            - draws a directed edge between prev and curr nodes
        Returns networkx graph object
        '''
        # extract file name of the pgn file -> to be used as 
        # the file name for the generated gml file
        self.pgnFileName=os.path.splitext(os.path.basename(path))[0]
        pgn=open(path)
        
        game=chess.pgn.read_game(pgn)
        diGraph=nx.DiGraph()
        while game:
            prev=game.board().fen()
            diGraph.add_node(prev)
            while game.next():
                game=game.next()
                curr=game.board().fen()
                diGraph.add_node(curr)
                diGraph.add_edge(prev, curr)
                prev=curr
            game=chess.pgn.read_game(pgn)
        return diGraph

    def generateGameNetwork(self, graphType='DiGraph'):
        '''
        generates a graph for the loaded game PGN
        returns a networkx graph object
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
        return diGraph        

    def generateGameGml(self, graph, dest='gml-base'):
        '''
        takes networkx graph object as input
        generates graphML file and saves it in dest folder with name self.pgnFileName
        '''
        # create GraphML file
        if dest=='gml-base':
            # if dest is not specified -> store gml file in default dir with default filename
            path=os.path.join(dest, self.pgnFileName+'.gml')
            nx.write_gml(graph, path)
        else:
            nx.write_gml(graph, dest)