def build_graph(edges, undirected=False):
    graph = {}
    
    # Generate a dictionary with all the nodes
    [graph.update({edge_1:[]}) for edge_1,edge_2 in edges]
    [graph.update({edge_2:[]}) for edge_1,edge_2 in edges]
    
    # Add all the edges
    [graph[edge_1].append(edge_2 )for edge_1,edge_2 in edges]
    # Make the edges reflexive if it is an undirected graph
    if undirected==True:
        [graph[edge_2].append(edge_1)for edge_1,edge_2 in edges]
    return graph