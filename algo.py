
def search(x, y):

    if grid[x][y] == 2:
        print('found at %d,%d' % (x, y))
        return True
    elif grid[x][y] == '#':
        print('wall at %d,%d' % (x, y))
        return False
    elif grid[x][y] == '.':
        print('visited at %d,%d' % (x, y))
        return False
    

    print('visiting %d,%d' % (x, y))

    # visited
    grid[x][y] = '.'

    # clockwise start by the right
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True

    return False

grid = [[' ', ' ' , ' ', ' ', '#', '#'],
        ['#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', 2, '#']]

bite = ['#', '#', '#', '#', '#', '#']

for c in bite:
    print(c,end = " ")
print()

for r in grid:
    for c in r:
        print(c,end = " ")
    print()

for c in bite:
    print(c,end = " ")
print()

search(0, 0)

for c in bite:
    print(c,end = " ")
print()
for r in grid:
    for c in r:
        print(c,end = " ")
    print()
for c in bite:
    print(c,end = " ")
print()