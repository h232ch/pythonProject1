


if __name__=="__main__":
    money = 1
    if money:
        print("get your taxi")
    else:
        print("work")

    money = 2000
    card = 1

    if money >= 3000 or card:
        print("get your taxi")
    else:
        print("work")


    print(1 in [1,2,3])
    print(1 not in [1,2,3])

    print('a' in ('a', 'b' 'c',))
    print('j' not in 'python')

    pocket = ['paper', 'cellphone', 'money1', 'card']
    if 'money' or 'card' in pocket:
        print("get texi")
    else:
        print('work')

    pocket = ['paper', 'handphone']
    card = 1
    if 'money' in pocket:
        print("get taxi")
    elif card:
        print("get taxi")
    else:
        print("work")


    pocket = ['paper', 'money', 'cellphone']
    if 'money' in pocket:
        pass
    else:
        print('put the card')

    if 'money1' in pocket : pass
    else : print("get your card")


    treeHit = 0
    while treeHit < 10:
        treeHit = treeHit + 1
        print("you attack tree %d times" % treeHit)
        if treeHit == 10:
            print("the tree is down")

    prompt = """
    . . . 1. Add
    . . . 2. Del
    . . . 3. List
    . . . 4. Quit
    . . .
    . . . Enter number: """

    number = 0
#   while number != 4:
    #   print(prompt)
    #   number = int(input())


    coffee = 10
    money = 300
    while money:
        print("I got money, give you coffee")
        coffee = coffee - 1
        print("the coffee remains %d" % coffee)
        if not coffee:
            print("there is no coffee, we are closed")
            break


    coffee = 10
    ownMoney = 3000

    while coffee:
        # money = int(input("please pay me : "))
        money = 300
        if money == 300:
            coffee = coffee - 1
            ownMoney = ownMoney - 300
            print("give customer coffee")
            print("the coffee is %d" % coffee)
        elif money > 300:
            coffee = coffee - 1
            ownMoney = ownMoney + (money - 300)
            print("give the less money %d" % (money - 300))
            print("give customer coffee")
            print("the coffee is %d" % coffee)
        else:
            print("money is not enough")
            print("there is nothing changed")

        a = 0
        while a < 10:
            a = a+1
            if a % 2 == 0:
                continue
            print(a)


        test_list = ['one', 'two', 'three']
        for i in test_list:
            print(i)

        marks = [90, 25, 67, 45, 80]

        number = 0
        for mark in marks:
            number = number +1
            if mark >= 60:
                print("%d student passed" % number)
            else:
                print("%d student failed" % number)

        for mark in marks:
            number = number + 1
            if mark < 60 : continue
            print("%d student passed" % number)


        a = range(10)
        print(a)

        sum = 0
        for i in range(1, 11):
            sum = sum + i

        print(sum)

        print(range(len(marks)))

        for number in range(len(marks)):
            if marks[number] < 60 : continue
            print("%d student passed" % (number + 1))


        for i in range(2, 10):
            for j in range(1, 10):
                print(i*j, end=" ")
            print('')

        a = [1,2,3,4,5]
        result = []
        for num in a:
            result.append(num * 3)
        print(result)

        result = [num * 3 for num in a]
        print(result)

        result = ["{0:0.4f}".format(num / 3) for num in a]
        print(result)

        result = [x*y for x in range(2,10)
                  for y in range(1,10)]





