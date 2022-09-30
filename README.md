# python-chessnet
Model the game of chess as a large complex network

1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [Features](#features)

## 1. Introduction<a name="introduction"/>
python-chess-network is a library for the study of the game of chess as a large complex network.

## 2. Dependencies<a name="dependencies"/>

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

* provides a utility to generate a graph (unweighted and directed) from a PGN file containing games of chess
  - individual board positions represented by FENs are nodes in the graph
  - a move in the game is represented by a directed edge between 2 nodes.
  ```python
  import gml # assumes you have gml.py in the same directory, or you know how to handle python modules.

  input_pgn_file='pgn-base/carlsen-caruana-2018.pgn'
  gmlCoverter=gml.GraphMLUtil()

  # generate graph object from pgn file
  diGraph=gmlCoverter.generateGamesNetwork(input_pgn_file)

  # generate graphml file from the graph object
  # (if no destination is provided - file is stored in gml-base directory 
  # with default file name)
  dest='gml-base/test-output.gml'
  gmlCoverter.generateGameGml(diGraph, dest)
  ```
