import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    return sum(
        state[i] != 0 and state[i] != goal[i]
        for i in range(9)
    )

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    moves = [-3, 3, -1, 1]

    for move in moves:
        new_pos = zero + move

        if 0 <= new_pos < 9:
            if move == -1 and zero % 3 == 0:
                continue
            if move == 1 and zero % 3 == 2:
                continue

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )
            neighbors.append(tuple(new_state))

    return neighbors

def astar(start):
    pq = [(heuristic(start), 0, start)]
    visited = set()
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, state = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        for nxt in get_neighbors(state):
            new_g = g + 1

            if nxt not in cost or new_g < cost[nxt]:
                cost[nxt] = new_g
                parent[nxt] = state
                h = heuristic(nxt)
                new_f = new_g + h
                heapq.heappush(pq, (new_f, new_g, nxt))

    return None

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
path = astar(start)

if path:
    for step, state in enumerate(path):
        g = step
        h = heuristic(state)
        f = g + h

        print("Move:", step)
        print("g =", g, "h =", h, "f =", f)

        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found")
