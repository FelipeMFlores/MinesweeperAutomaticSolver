# find_all_flags
# for all cells:
#     if a number:
#         if number of covered neighbors cells + flag neighbors ==  numbrt in cell:
#             flags += flag all neighbors
#              repeat all

# find_all_plays
# for all cells:
#     if a number:
#         if number of neighbors flags == number in cell:
#             plays += click all neighbors
#             repeat all

# -1 == flag/will be flaged, -2 == covered, -3 == will be clicked,
# 0 == empty uncovered, number = number
FLAG = -1
COVERED = -2
WILL_CLICK = -3
EMPTY = 0

#neighbors( cell ): devolve um array com todos os vizinhos da celula
def get_neighbors(matrix, cell):
    neighbors_list = []
    for i in range(-1, 2):
        for k in range(-1, 2):
            if i == 0 and k == 0:
                continue
            x, y = cell[0] + i, cell[1] + k
            if x < 0 or y < 0:
                continue
            try:
                neighbors_list.append(matrix[x][y])
            except IndexError:
                pass
    return neighbors_list

def set_neighbors(matrix, cell, new_value):
    new_cells = []
    for i in range(-1, 2):
        for k in range(-1, 2):
            if i == 0 and k == 0:
                continue
            x, y = cell[0] + i, cell[1] + k
            if x < 0 or y < 0:
                continue
            try:
                if matrix[x][y] == COVERED:
                    matrix[x][y] = new_value
                    new_cells.append((x, y))
            except IndexError:
                pass
    return new_cells

def find_all_flags(matrix):
    flags = []
    changed = True
    while changed is True:
        changed = False
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                cell = matrix[i][k]
                if cell > 0:
                    neighbors_list = get_neighbors(matrix, (i, k))
                    nflags = neighbors_list.count(FLAG)
                    ncovered = neighbors_list.count(COVERED)
                    if ncovered != 0 and ncovered + nflags == cell:
                        new_flags = set_neighbors(matrix, (i, k), FLAG)
                        if new_flags != []:
                            flags.extend(new_flags)
                            changed = True
    return flags

def find_all_plays(matrix):
    plays = []
    changed = True
    while changed is True:
        changed = False
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                cell = matrix[i][k]
                if cell > 0:
                    neighbors_list = get_neighbors(matrix, (i, k))
                    nflags = neighbors_list.count(FLAG)
                    if nflags == cell:
                        new_plays = set_neighbors(matrix, (i, k), WILL_CLICK)
                        if new_plays != []:
                            plays.extend(new_plays)
                            changed = True
    return plays


def get_flags_and_plays(matrix):
    new_flags = find_all_flags(matrix)
    new_plays = find_all_plays(matrix)
    return new_flags, new_plays
