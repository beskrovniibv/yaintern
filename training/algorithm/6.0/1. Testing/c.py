#! /usr/bin/python python python3

font = {
    ('#',): 'I',
    ('###','#.#','###'): 'O',
    ('###', '#.#'): 'C',
    ('##', '#.'): 'L',
    ('###', '.#.', '###'): 'H',
    ('####', '.#.#', '.###'): 'P',
}


def empty_line(value):
    return value.count(".") == len(value)


def main():
    n = int(input())
    display = [input() for _ in range(n)]
    shrink = []
    prev = ""
    for line in display:
        if not prev or line != prev:
            shrink.append(line)
            prev = line
    while shrink and empty_line(shrink[0]):
        shrink.pop(0)
    while shrink and empty_line(shrink[-1]):
        shrink.pop(-1)
    rotated = [''.join(row) for row in list(zip(*shrink[::-1]))]
    shrink = []
    prev = ""
    for line in rotated:
        if not prev or line != prev:
            shrink.append(line)
            prev = line
    while shrink and empty_line(shrink[0]):
        shrink.pop(0)
    while shrink and empty_line(shrink[-1]):
        shrink.pop(-1)
    print(font.get(tuple(shrink), 'X'))

if __name__ == "__main__":
    main()
