from _collections import deque

graph0 = {"Kirill": ["Bob", "Alice", "Clare"],
          "Bob": ["Anj", "Peggy"],
          "Clare": ["Tom", "Johnny"],
          "Alice": ["Peggy", "Jacob"],
          "Peggy": [],
          "Johnny": [],
          "Tom": [],
          "Anj": [],
          "Jacob": ["Tom"]}


def search(name):
    search_deque = deque()
    search_deque += graph0[name]
    searched = []
    # print(search_deque)
    while search_deque:
        person = search_deque.popleft()
        if person == "Johnny":
            return True
        else:
            for o in graph0[person]:
                if o in search_deque:
                    graph0[person].remove(o)
            search_deque += graph0[person]
            searched.append(person)
            # print(search_deque)
            # print(searched)


if search("Kirill"):
    print("Продавец найден")
else:
    print("Продавец не найден")

# Dijkstra's algorithm
infinity = float("inf")


def find_lowest_cost_node(costs, processed):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph, costs, parents, processed):
    node = find_lowest_cost_node(costs, processed)
    result = []
    while node is not None:
        cost = costs[node]
        # print(cost)  # 2
        neighbors = graph[node]
        # print(neighbors)  # a: 8, c: 7
        if len(neighbors) == 0:
            result.append(cost)
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    result_cost = result[0]
    for i in range(0, len(result) - 1):
        if result[i] < result[i + 1]:
            result_cost = result[i]
    return result_cost


# Graph1
graph1 = {}
graph1["start"] = {}
graph1["start"]["a"] = 5
graph1["start"]["b"] = 2

graph1["a"] = {}
graph1["a"]["d"] = 4
graph1["a"]["c"] = 2

graph1["b"] = {}
graph1["b"]["a"] = 8
graph1["b"]["c"] = 7

graph1["c"] = {}
graph1["c"]["fin"] = 1

graph1["d"] = {}
graph1["d"]["c"] = 6
graph1["d"]["fin"] = 3

graph1["fin"] = {}

costs1 = {"a": 5, "b": 2, "c": infinity, "d": infinity, "fin": infinity}

parents1 = {"a": "start", "b": "start", "fin": None}
processed1 = []

# Graph2
graph2 = {}
graph2["start"] = {}
graph2["start"]["b"] = 10

graph2["b"] = {}
graph2["b"]["c"] = 20
graph2["c"] = {}
graph2["c"]["fin"] = 30
graph2["c"]["d"] = 1
graph2["d"] = {}
graph2["d"]["b"] = 1
graph2["fin"] = {}

costs2 = {"b": 10, "c": infinity, "d": infinity, "fin": infinity}
parents2 = {"b": "start", "fin": None}
processed2 = []

print("Кратчайший путь: " + str(dijkstra(graph1, costs1, parents1, processed1)))
print("Кратчайший путь: " + str(dijkstra(graph2, costs2, parents2, processed2)))
