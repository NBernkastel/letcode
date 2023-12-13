grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]

def equal_pairs(grid: list[list[int]]) -> int:
    state_row = {}
    state_col = {}
    for i in range(len(grid)):
        if tuple(grid[i]) not in state_row:
            state_row[tuple(grid[i])] = 1
        else:
            state_row[tuple(grid[i])] += 1
        column = []
        for j in range(len(grid)):
            column.append(grid[j][i])
        if tuple(column) not in state_col:
            state_col[tuple(column)] = 1
        else:
            state_col[tuple(column)] += 1
    state_row_val = tuple(state_row.values())
    state_col_val = tuple(state_col.values())
    state_row_key = tuple(state_row.keys())
    state_col_key = tuple(state_col.keys())

    res = 0
    for i in range(len(state_row_key)):
        for j in range(len(state_col_key)):
            if state_row_key[i] == state_col_key[j]:
                if state_row_val[i] == 1 and state_col_val[j] == 1:
                    res += 1
                else:
                    res += state_row_val[i] * state_col_val[j]
    return res


print(equal_pairs(grid))
