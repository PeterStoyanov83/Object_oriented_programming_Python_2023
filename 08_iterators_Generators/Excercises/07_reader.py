def read_next(*args):
    for el in args:  # string
        for sub_el in el:
            yield sub_el

