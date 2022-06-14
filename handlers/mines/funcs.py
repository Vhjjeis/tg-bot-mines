import random


def func_chunks_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def func_get_new_field(q_cells, q_mines):
    cells = list(range(q_cells * q_cells))
    for i in random.sample(cells, q_mines):
        cells[i] = 'm'
    field = list(func_chunks_generators(cells, q_cells))
    return field


