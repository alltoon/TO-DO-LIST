
def header(row0: int, row1: int, row2: int, row3: int):
    head = "╔"
    for i in range(row0 +2): head += "═"
    head += "╦"
    for _ in range(row1 + 2): head += "═"
    head += "╦"
    for _ in range(row2 + 2): head += "═"
    head += "╦"
    for _ in range(row3 + 2): head += "═"
    head += "╗"

    return head


def middle(row0: int, row1: int, row2: int, row3: int):
    mid = "╠"
    for i in range(row0 + 2): mid += "═"
    mid += "╬"
    for _ in range(row1 + 2): mid += "═"
    mid += "╬"
    for _ in range(row2 + 2): mid += "═"
    mid += "╬"
    for _ in range(row3 + 2): mid += "═"
    mid += "╣"
    return mid


def footer(row0: int, row1: int, row2: int, row3: int):
    foot = "╚"
    for i in range(row0 + 2): foot += "═"
    foot += "╩"
    for _ in range(row1 + 2): foot += "═"
    foot += "╩"
    for _ in range(row2 + 2): foot += "═"
    foot += "╩"
    for _ in range(row3 + 2): foot += "═"
    foot += "╝"
    return foot


def range_space_cell(n_max, row): # n_max => row size max
    if len((str(row))) < n_max:
        space_cell = "".join(" " for _ in range(n_max - len((str(row)))))
        return str(space_cell)
    else:
        return str("")

def count_max_row(n, all_row):  # n => row size
    for row in all_row:
        row_max = 0
        if len(str(row[n])) >= row_max:
            row_max = len(str(row[n]))
    return row_max


def chart(all_row):
    c =0
    print(header(count_max_row(0, all_row), count_max_row(1, all_row), count_max_row(2, all_row), count_max_row(3, all_row)))
    for row in all_row:
        if c!=0:
            print(middle(count_max_row(0, all_row), count_max_row(1, all_row), count_max_row(2, all_row), count_max_row(3, all_row)))
        print('║ {0} ║ {1} ║ {2} ║ {3} ║'.format(str(row[0]) + str(range_space_cell(count_max_row(0, all_row), row[0])),
                                                 str(row[1]) + str(range_space_cell(count_max_row(1, all_row), row[1])),
                                                 str(row[2]) + str(range_space_cell(count_max_row(2, all_row), row[2])),
                                                 str(row[3]) + str(range_space_cell(count_max_row(3, all_row), row[3]))))
        c +=1
    print(footer(count_max_row(0, all_row), count_max_row(1, all_row), count_max_row(2, all_row), count_max_row(3, all_row)))
