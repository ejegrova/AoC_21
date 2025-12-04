import math


def load_data(file):
    """
    loads data from file

    :param file: input file
    :return: distances of the vertices, each vertex determines distance when entering it
    :rtype: list of lists
    """
    with open(file, "r", ) as f:
        data = []
        for line in f:
            data.append(list(map(int, line.strip("\n"))))
    return data


def best_path():
    """
    dijkstra algorithm
    1) pick a vertex with the shortest current cost, visit it, and add it to the visited vertices set
    2) update the costs of all its adjacent vertices that are not visited yet.
        For every edge between n and m where m is unvisited,
        if the cheapestPath(s, n) + cheapestPath(n,m) < cheapestPath(s,m),
        update the cheapest path between s and m to equal cheapestPath(s,n) + cheapestPath(n,m)
    """
    while not all(d["visited"] for d in graph.values()):
        # get unvisited vertex with shortest cost
        costs = [(key, val["cost"]) for key, val in graph.items() if not val["visited"]]
        minimal_vertex_cost = min(costs, key=lambda t: t[1])

        # visit vertex
        graph[minimal_vertex_cost[0]]["visited"] = True

        # update cost and path of neighbours
        for neighbour in graph[minimal_vertex_cost[0]]["neighbours"]:
            if not graph[neighbour]["visited"]:
                new_cost = minimal_vertex_cost[1] + graph[neighbour]["risk_level"]
                if new_cost < graph[neighbour]["cost"]:
                    graph[neighbour]["cost"] = new_cost
                    set_path(neighbour, graph[minimal_vertex_cost[0]]["path"])


def set_path(vertex, path_to_previous_vertex):
    """
    Change path to vertex with different path

    :param str vertex: id of the vertex
    :param str path_to_previous_vertex: path from different vertex
    """
    graph[vertex]["path"] = f"{path_to_previous_vertex}{vertex},"


def initialize_graph():
    """
    Set neighbours, costs, risk_level, visited and path for all vertices

    :return: dict with necessary information, key-value pair looks like:
        '43': {'cost': inf, 'risk_level': 3, 'neighbours': {'42', '53', '33', '44'}, 'visited': False, 'path': ''}
    :rtype: dict of dict
    """
    graph = {}
    for row, line in enumerate(data):
        for col, num in enumerate(line):
            neighbours = []
            for i in [0, -1], [0, 1], [-1, 0], [1,0]:   # find all neighbours for single vertex
                if (row + i[0]) >= 0 and (row + i[0]) < len(data) and (col + i[1]) >= 0 and (col + i[1]) < len(data):
                    neighbours.append(create_id_from_vertex_position(row, col, i[0], i[1]))
            main_vertex = create_id_from_vertex_position(row, col, 0, 0)
            graph[main_vertex] = {"cost": math.inf, "risk_level": num, "neighbours": set(neighbours), "visited": False, "path": ""}

    return graph


def create_id_from_vertex_position(row, col, row_value, col_value):
    """
    Create string id that is composed of the row and column position,
    e.g. row = 2, col=99, row_value=-1, col_value=0
        neighbour = "0199"

    :param int row: index of the row
    :param int col: index of the column
    :param int row_value: value to add to row value
    :param int col_value: value to add to column value
    :return: id of the neighbour consisting of 4 chars
    :rtype: str
    """
    neighbour = ""
    for tab_pos, value in (row, row_value), (col, col_value):
        updated_value = tab_pos + value
        if len(str(updated_value)) < 2:
            string = f"0{str(updated_value)}"
        else:
            string = str(updated_value)
        neighbour = f"{neighbour}{string}"

    return neighbour


if __name__ == "__main__":
    data = load_data("15.txt")
    graph = initialize_graph()

    graph["0000"]["cost"] = 0
    set_path("0000", "")

    best_path()

    last_vortex = sorted(graph.keys())[-1]
    print(f"path: {graph[str(last_vortex)]['path']}")
    print(f"total risk of the path: {graph[str(last_vortex)]['cost']}")
