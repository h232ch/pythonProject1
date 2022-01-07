


if __name__ == "__main__":
    a = 3 # a라는 메모리 값에 3을 저장
    b = 3
    print(a is b) # 같은 정수형 메모리를 바라보기 때문에 참
    # 3이라는 정수형 객체의 레퍼런스 카운트는 현재 2 (a, b)다

    a, b = 'python', 1
    print(a, b)

    (a, b) = ['python', 'life']
    print(a,b)
    print(a)

    a = 3
    b = 5
    a, b = b, a
    print(a, b)

    a = [1,2,4]
    b = a
    a[1] = 5
    print(a, b) # 값이 동일한 이유? a, b가 서로 같은 메모리값 참조

    a = [1,2,3]
    b = a[:] # 메모리를 참조하지 않는 얇은 복사
    a[1] = 4
    print(a, b)

    from copy import copy
    b = copy(a) # it's samw with a[:]

    a[1] = 1000
    print(a, b)

    print(a is b)
