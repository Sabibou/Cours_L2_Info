import random
import Special_Graphs

import os
import graphviz as gv

"""A vertex is a string.
A graph is a dictionary; its keys are vertices and the value associated to a
key/vertex u is the set of neighbors of u in G.
"""

def extract_graph_from_file(file):
    """Takes a file name as input and extracts the graph inside it.
    The file is composed of n lines, where n is the total number of vertices.
    Each line is of the form u:v1:v2:...:vk where u is a vertex and the
    vi's are its neighbors. If u has no neighbor, the corresponding line is u:
    This function returns a dictionary representing the graph:
    Its keys are vertices and its values are the sets of neighbors
    of each vertex. """
    with open(file, "r") as f:
        d = {}
        for line in f:
            line = line.strip()
            line = line.split(":")
            if (len(line) == 1):
                d[line[0]] = set()
            else:
                d[line[0]] = set(line[1:])
        
        return d

def set_of_vertices(graph):
    """Returns the set of vertices of the graph."""
    return set(graph.keys())


def set_of_neighbors(graph, u):
    """Returns the set of neighbors of vertex u in the graph."""
    return set(graph[u])


def degree_of(graph, u):
    """Returns the numbers of neighbors of vertex u in the graph."""
    return len(graph[u])


def are_neighbors(graph, u, v):
    """Boolean function returning True if u and v are neighbors in the graph.
     Returns False otherwise."""
    return v in graph[u]


def number_of_vertices(graph):
    """Returns the number of vertices of the graph."""
    return len(graph)


def number_of_edges(graph):
    """Returns the number of edges of the graph.
    We suppose that it is NON directed."""
    return sum([len(graph[u]) for u in graph]) // 2


def is_symmetric(graph):
    """Boolean function returning True if the dictionary representing the graph
    is symmetric: u is a neighbor of v iff v is a neighbor of u.
    Returns False otherwise and print a non symmetric couple."""
    for u in graph:
        for v in graph[u]:
            if u not in graph[v]:
                print(f"Non symmetric couple: {u}, {v}")
                return False
    return True


def bfs(graph, r):
    """Makes the BFS of the graph from vertex r. Returns a tuple
    (parent, d, color)."""
    parent = {r: None}
    d = {r: 0}
    color = {r: "gray"}
    queue = [r]
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if v not in color:
                color[v] = "gray"
                d[v] = d[u] + 1
                parent[v] = u
                queue.append(v)
        color[u] = "black"
    return parent, d, color


def color_graph_by_list(graph, list_of_vertices):
    """Takes as input a graph and a list of its vertices. This function colors
    the graph with this list and returns a tuple (c, color) where:
     + color is the constructed coloration (a dictionary whose keys are the
     vertices and values are colors (integers > 0)) and
     + c is the number of colors used by the coloration color."""
    color = {}
    c = 0
    for u in list_of_vertices:
        color[u] = c
        c += 1
    return c, color


def color_graph_by_random_lists(graph, number_of_iterations=1):
    """Takes as input a graph, and an integer number_of_iterations.
    Runs number_of_iterations times the coloring function of the graph on
    random lists of vertices of the graph and returns the best coloring found
    (the one using the lowest number of colors)."""
    best_coloring = {}
    best_c = float("inf")
    for i in range(number_of_iterations):
        list_of_vertices = list(graph.keys())
        random.shuffle(list_of_vertices)
        c, color = color_graph_by_list(graph, list_of_vertices)
        if c < best_c:
            best_c = c
            best_coloring = color
    return best_coloring


def is_stable(graph, set_s):
    """Boolean function taking as input a graph and a set of vertices.
    It returns True if this set is a stable of the graph (there is no edge
     between vertices of this set in the graph).
     Returns False otherwise."""
    for u in set_s:
        for v in set_s:
            if are_neighbors(graph, u, v):
                return False
    return True


def is_proper_coloring(graph, color):
    """Takes as input a graph and a coloring (a dictionary having the set of
    vertices as keys and colors (integers > 0) as values).
    Returns True if color is a proper coloring of the graph.
    Returns False otherwise and print a message to indicate the error."""
    for u in graph:
        for v in graph[u]:
            if color[u] == color[v]:
                print(f"Error: {u} and {v} have the same color.")
                return False
    return True

def render_graph(graph, color=None, filename="graph"):
    with open(filename + ".dot", "w") as f:
        f.write("digraph G {\n")
        for u in graph:
            for v in graph[u]:
                if color is None:
                    f.write(f"{u} -> {v};\n")
                else:
                    f.write(f"{u} -> {v} [color={color[u]}];\n")
        f.write("}\n")
    os.system(f"dot -Tpng {filename}.dot -o {filename}.png")



# Special_Graphs.hypercube_graph(3)  # To construct a hypercube(d)
global_graph = extract_graph_from_file("hypercube.txt")
print("------ BFS from 000:", bfs(global_graph, "000"))
print(f"------ Is the graph symmetric? {is_symmetric(global_graph)}")
global_coloring_of_the_graph = color_graph_by_random_lists(global_graph, 4)
print(global_coloring_of_the_graph)
# resultG["000"] = resultG["010"] # To force an error in H3 graph.
print(f"-- Is it a valid coloring? "
      f"{is_proper_coloring(global_graph, global_coloring_of_the_graph)}")

render_graph(global_graph)
