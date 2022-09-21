import gml

input_pgn_file='pgn-base/immortal-game.pgn'
gmlCoverter=gml.GraphMLUtil()

# load pgn file
gmlCoverter.loadSinglePgnFile(input_pgn_file)

# generate graph object from the loaded pgn
diGraph=gmlCoverter.generateGameNetwork()

# generate graphml file from the graph object
gmlCoverter.generateGameGml(diGraph)