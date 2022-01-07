
# 튜플은 리스트와 달리 값을 변경할 수 없다



if __name__ == "__main__":
    t1 = ()
    t2 = (1, 2, 3)
    t3 = 1, 2, 3
    t4 = ('a', 'b', 'c',)

    # indexing
    t1 = (1, 2, 'a', 'b',)
    print(t1[0])
    print(t1[3])

    # splicing
    t2 = (3, 4)
    print(t2[:1])

    # add
    t2 = 4, 5
    print(t1 + t2)

    print(t2 * 4)

