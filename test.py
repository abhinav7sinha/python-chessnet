import gml
input_pgn_file='pgn-base/immortal-game.pgn'
gmlCoverter=gml.GraphMLUtil()
gmlCoverter.loadSinglePgnFile(input_pgn_file)
gmlCoverter.generateGameGml()