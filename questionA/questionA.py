def isOverlap(x,y):
    return 'overlap' if y[0] <= x[0] < y[1] or y[0] < x[1] <= y[1] else 'no overlap'

if __name__ == '__main__':
    z = [(1,2),(1,3)]
    print(isOverlap(z[0], z[1]))

    z = [(1,2),(2,3)]
    print(isOverlap(z[0], z[1]))

    z = [(3,4),(1,3)]
    print(isOverlap(z[0], z[1]))

    z = [(3,4),(1,2)]
    print(isOverlap(z[0], z[1]))
    z = [(3,4),(3,4)]
    print(isOverlap(z[0], z[1]))
