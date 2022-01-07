# 집합을 쉽게 처리하기 위해 만들어짐
# 중복 허용안함
# 순서가 없음
# 중복 제거를 위해 종종 사용됨



if __name__ == '__main__':
    
    # list to set
    s1 = set([1,2,3])
    print(s1)

    # str to set
    s2 = set("Hello")
    print(s2)

    s1 = set([1,2,3])
    l1 = list(s1)
    print(l1[0])

    # 교집합, 합집합, 차집합
    s1 = set([1,2,3,4,5,6])
    s2 = set([4,5,6,7,8,9])

    print(s1 & s2)
    print(s1.intersection(s2))

    print(s1 | s2)
    print(s1.union(s2))

    print(s1 - s2)
    print(s1.difference(s2))

    s1 = set([1,2,3])
    s1.add(4)

    print(s1)
    s1 = set([1,2,3, 4])
    s1.update([4,5,6])
    print(s1)

    s1 = set([1,2,3])
    s1.remove(3)
    print(s1)


