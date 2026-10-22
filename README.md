k-Betweenness Centrality Measure using BFS Algorithm

ABOUT- 1) This project helps to understand k-betweenness centrality in Python using NetworkX and Breadth 
       First Search(BFS) algorithm.
       2) Betweenness centrality measures how often a node lies on the shortest path between pairs of 
       other nodes.
       3) In k-betweenness only shortest path with a length less than or equal to the horizon k (as a
       limit) are counted.
       4) This project uses a BFS approach along with dependency accumulation based on Brandes algorithm to
       calculate the centrality values.

Objectives-1) Implementation and explanation of the k-Betweenness centrality using BFS.
           2) Consider shortest paths length to atmost k.
           3) Implementation of various datasets
           4) Calculate centrality scores for every node
           5) Evaluate the algorithm on different real world networks.

Programs Used-1) Python 
              2) NetworkX
              3) collections(deque) for BFS operations on double ended queue

Datasets-The code supports various datasets. They are listed below:-
         1) Karate Club-A social network in Python.
         2) Dolphins-A social network showing association in Dolphins.
         3) Football-A network showing connection between college football teams.
         4) PolBooks-A network of Political books.
         5) Reachability-A network to represent airport reachability network.
         *These datasets must be available locally in required file formats.

Pre-requisite installations-1) Install Python 3.
                            2) Install NetworkX- Use the following command in the terminal
                                                  " pip install Networkx "

How to run-1) Download or copy this repository.
           2) Place the Python code and the required dataset in the same directory.
           3) Open a terminal in the Python directory.
           4) Run : " python k_betweenness_centrality.py "
           *The program runs and displays the top 10 nodes with the highest k-betweenness centrality
           scores for k=2, k=3 and k=5 for each dataset.

Algorithm Overview- The implementation follow these steps:
                    1) Initialize -      All node scores are set to zero initially.
                    2) BFS Traversal-   Each node is treated as a source node one by one and all the
                                        other nodes are taken as pairs and shortest paths are explored
                                        upto a distance k.
                    3) Shortest paths-  Store distances and the number of shortest paths and also the 
                                        predecessor nodes.
                    4) Dependency-      The visited nodes are then traversed backwards to calculate their 
                                        contributions on other nodes.
                    5) Calculate Scores-Add the dependencies to obtain the centrality of each node.
                    6)Normalisation-    Optionally apply the Standard Brandes-style scaling when 
                                        normalised=True.

Expected Input- The program takes the following inputs:
                1) G- A networkX graph representing the network.
                2) k- Shortest path limit for distances to consider (e.g. k=2,3 or 5)
                3) normalized- Optional Boolean value (True or False)
                4) Dataset files- Graph files for datasets used
                  ( dolphins.gml ,football.gml ,polbooks.gml ,reachability.txt)
                *The Karate Club is provided directly in NetworkX and does not require external file.

Expected output- The Program prints the number of nodes and edges in each dataset, followed by the 
                 top 10 nodes and their centrality values for each value of k.
                 Values also depend upon the dataset used.

Notes and Limitations- 1) Designed for unweighted Graphs
                       2) The value of k must be greater than or equal to 2.
                       3) External dataset files must be kept in same directory and in compatible 
                          format.
                       4) For disconnected graphs only reachable graphs contribute in the shortest paths.
                       5) Scores are normalized by standard Brandes-style type scaling (not necessarily to 1)

Author- Malaya Gupta    and      Ansh Chaturvedi
        Roll no- 36              Roll no-12
        Network Science 
