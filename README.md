# python-chess-network
Model the game of chess as a large complex network

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Features](#features)

## 1. Introduction<a name="introduction"/>
python-chess-network is a library for the study of the game of chess as a large complex network.

## 2. Installation<a name="installation"/>

* Python3 - [Download and Install Python3](https://www.python.org/downloads/). You can also use your system's package manager to install the latest stable version of python3.
* Now Install the following packages:</br>
    1. [networkx](https://github.com/networkx/networkx)
        ```bash
        pip install networkx
        ```
    2. [python-chess](https://github.com/niklasf/python-chess)
        ```bash
        pip install chess
        ```

## 3. Features<a name="features"/>

* provides a utility to generate a graph (unweighted and directed) from a PGN file
  - individual board positions represented by FENs are nodes in the graph
  - a directed edge between 2 nodes represents a move in the game of chess.
  ```python
  import gml

  input_pgn_file='pgn-base/immortal-game.pgn'
  gmlCoverter=gml.GraphMLUtil()

  # load PGN file
  gmlCoverter.loadSinglePgnFile(input_pgn_file)

  # generate graph object from the loaded pgn
  diGraph=gmlCoverter.generateGameNetwork()

  # generate graphml file from the graph object
  gmlCoverter.generateGameGml(diGraph)
  ```
