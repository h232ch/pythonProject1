

if __name__ == "__main__":
    a = []
    b = [1,2,3,4]
    c = ['life', 'is']
    d = [1, 2, ['Life', 'is']]

    print(a)
    print(b)
    print(b[2])
    print(b[3])
    print(c)
    print(c[1])
    print(d)
    print(d[2][0])

    a = [1, 2, ['a', 'b', ['life', 'is']]]
    print(a[2][2][1])

    a = [1,2,3,4,5]
    print(a[0:3])
    print(a[1:4])

    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a + b)

    a = [1, 2, 3]
    a[2] = 4
    print(a)
    a[1:2] = ['a', 'b', 'c']
    print(a)
    a[1:1] = ['a', 'b', 'c']
    print(a)
    a[1] = ['it\'s different', 'and', 'you']
    print(a)
    a[1:2] = []
    print(a)

    a = [1, 2, 3]
    print(str(a[1]) + ' it\'s the way to add ')

    a = [1, 2, 3]
    a.append(4)
    print(a)
    a.append([5,6])
    print(a)
    a = [3,5,2,4,5,6,2]
    a.sort()
    print(a)
    a = [1,2,3,4,5,]
    print(a.index(4))
    a = [1,2,3,4,5]
    a.insert(0, 4) # on 0, insert 4
    print(a)
    a.insert(3, 10)
    print(a)
    a.sort()
    print(a)
    a = [1,2,3,4,65,6]
    a.remove(65)
    print(a)
    print(a.pop())
    print(a.pop())
    print(a.pop())

    print(a)








