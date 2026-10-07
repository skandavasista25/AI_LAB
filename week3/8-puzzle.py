nodes = 0
def dfs(state, goal, depth, path):
    global nodes
    nodes += 1
    if state == goal:
        return path
    if depth == 0:
        return None
    zero = state.index(0)
    moves = [-3, 3, -1, 1]
    for move in moves:
        new = zero + move
        if 0 <= new < 9:
            if move == -1 and zero % 3 == 0:
                continue
            if move == 1 and zero % 3 == 2:
                continue
            s = list(state)
            s[zero], s[new] = s[new], s[zero]
            s = tuple(s)
            if s not in path:
                result = dfs(s, goal, depth - 1, path + [s])
                if result:
                    return result
    return None
def IDS(start, goal):
    global nodes
    depth = 0
    while True:
        nodes = 0
        result = dfs(start, goal, depth, [start])
        print(f"Depth limit {depth}: Nodes = {nodes}")
        if result:
            return result, depth, nodes
        depth += 1
start = (1, 2, 3,
         0, 4, 6,
         7, 5, 8)
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
solution, found_depth, nodes_at_found_depth = IDS(start, goal)
for i in range(len(solution)):
    state = solution[i]
    if i == 0:
        move_name = "START"
    else:
        prev_zero = solution[i - 1].index(0)
        curr_zero = state.index(0)
        diff = curr_zero - prev_zero
        if diff == -3:
            move_name = "Move Up"
        elif diff == 3:
            move_name = "Move Down"
        elif diff == -1:
            move_name = "Move Left"
        elif diff == 1:
            move_name = "Move Right"
    print(move_name)
    print(state[:3])
    print(state[3:6])
    print(state[6:])
    print()
print(f"Total moves : {len(solution) - 1}")
print(f"Solution depth : {found_depth}")
print(f"Nodes at solution depth : {nodes_at_found_depth}")

