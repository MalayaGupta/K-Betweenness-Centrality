from collections import deque #deque is double ended queue (provides O(1) for append and pop) used in BFS
import networkx as nx


def k_betweenness_centrality(G, k, normalized=False):
    """Exact bounded-distance k-betweenness for an unweighted graph.

    Only shortest paths of length <= k contribute.
    Returns a dict {node: centrality}.
    """
    if k < 1:
        raise ValueError("k must be >= 1")

    CB = dict.fromkeys(G, 0.0) #Centrality Betweenness Dictionary, iterates through all nodes in G and assigns 0.

    for source in G:
        #empty list, LIFO, later used to pop off nodes in reverse (farthest to closest distance)
        stack = [] 
        #Dictionary with key 'v' and value initially empty list, stores immediate predecessors of v on all shortest paths
        pred = {v: [] for v in G}
        #Number of shortest paths to node v, initially 0 
        sigma = dict.fromkeys(G, 0.0)
        #Stores distance (no. of hops) from node v, initially -1 to show unvisited node 
        dist = dict.fromkeys(G, -1)
        sigma[source] = 1.0 #
        dist[source] = 0 #
        q = deque([source]) #

        # Bounded BFS: never expand beyond distance k.
        while q:
            v = q.popleft()
            stack.append(v)
            if dist[v] >= k:
                continue

            for w in G[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)

        # Brandes dependency accumulation.
        delta = dict.fromkeys(G, 0.0)
        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != source:
                CB[w] += delta[w]

    # Undirected graphs count each unordered pair twice.
    if not G.is_directed():
        CB = {v: value / 2.0 for v, value in CB.items()}

    # Standard Brandes scaling. For bounded BC this is a scaling for
    # comparability, not a graph-specific maximum normalization.
    if normalized:
        n = len(G)
        if n > 2:
            scale = 1.0 / ((n - 1) * (n - 2))
            if not G.is_directed():
                scale *= 2.0
            CB = {v: value * scale for v, value in CB.items()}

    return CB


def k_betweenness_value(G, node, k, normalized=False):
    """Return k-betweenness value for one node."""
    if node not in G:
        raise nx.NetworkXError("node is not in G")
    return k_betweenness_centrality(G, k, normalized)[node]


def evaluate_dataset(G, name, ks=(2, 3, 5)):
    print(f"\n{name}: n={len(G)}, m={G.number_of_edges()}")
    for k in ks:
        scores = k_betweenness_centrality(G, k=k)
        top10 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]
        print(f"k={k}: {top10}")


if __name__ == "__main__":
    # Karate is included directly in NetworkX.
    G_karate = nx.karate_club_graph()

    # Supply these local files from your dataset folder.
    # Adjust label/format arguments to match your downloaded files.
    G_dolphins = nx.read_gml("dolphins.gml", label="label")
    G_football = nx.read_gml("football.gml", label="id")
    G_polbooks = nx.read_gml("polbooks.gml", label="id")
    G_reachability = nx.read_edgelist(
        "reachability.txt", create_using=nx.DiGraph()
    )

    datasets = [
        (G_karate, "Karate"),
        (G_dolphins, "Dolphins"),
        (G_football, "Football"),
        (G_polbooks, "PolBooks"),
        (G_reachability, "Reachability"),
    ]

    for G, name in datasets:
        evaluate_dataset(G, name)
