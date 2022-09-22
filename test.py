import gml

input_pgn_file='pgn-base/carlsen-caruana-2018.pgn'
gmlCoverter=gml.GraphMLUtil()

# generate graph object from pgn file
diGraph=gmlCoverter.generateGamesNetwork(input_pgn_file)

# generate graphml file from the graph object
gmlCoverter.generateGameGml(diGraph)