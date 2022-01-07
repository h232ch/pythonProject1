
# Associate array, Hash
# Key, Value 자료형
# 리스트나 튜플처럼 순차적으로 값을 검색하지 않음
# then key를 통해 value를 검색
# 동일한 키 값을 가지면 앞의 값이 무시됨





if __name__ == "__main__":
    a = {'name' : 'pay', 'phone' : '01093860698', 'birth' : '1108'}
    print(a)
    print(a['name'])

    a = {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"}
    grade = {'pay':10, 'julliet':99}
    print(grade['pay'])
    print(grade['julliet'])

    a = {1: 'a'}
    a[2] = 'b'
    print(a)

    a['name'] = 'pay'
    print(a)
    a[3] = [1,2,3,4]
    print(a)

    
    a = {1:'a', 1:'b'}
    print(a)

    # 키값으로 튜플(O), 리스트(X) 리스트는 변하는 값이기 때문
    a = {(1,2):"test"}
    print(a)
    print(a[(1,2)])


    a = {'name' : 'pay', 'phone' : '01o93860698', 'birth': '880701'}
    print(a.keys())
    print(list(a.keys()))
    print(a.values())

    a = ([1,2,3,4], 10)
    print(a[0][1])
    a[0][1] = 'janem'
    print(a)
    # a[1] = 11 # error occured
    # print(a)

    a = {'name' : 'pay', 'phone' : '01o93860698', 'birth': '880701'}
    print(a.items())

    a.clear()
    print(a)

    a = {'name' : 'pay', 'phone' : '01o93860698', 'birth': '880701'}
    print(a.get('name'))
    print(a['name'])
    # there is difference at error page,
    # a.get doesn't make error if there is no key
    # but a['name'] make trace back error

    print('name' in a)
    print('email' in a)

    


