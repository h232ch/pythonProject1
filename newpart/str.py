
import sys

def print_hi(str):
    print(str)


def sum(a, b):
    print (a + b)


if __name__ == '__main__':
    msg = 'message'
    print_hi(msg)

    a = 1
    b = 2
    print (a+b)

    if a < b:
        print("a is greater than 1")

    for a in [1, 2, 3]:
        print (a)

    i = 0
    while i < 3:
        i = i + 1
        print(i)

    sum(10, 20)

    print (2 ** 4)
    print (7 % 3)
    print (7 / 3)
    print (7 // 3)

    say = "\"Python is very eaty \" he says"
    food = 'Pyton\'s favoriate food is pear'

    multiline = "Life is too short\nYou need python"
    print (multiline)
    multiline = """
    Life is too short
    You need python
    """
    print (multiline)
    head = "Python"
    tail = " is fun!"
    print (head + tail)
    a = "Python"
    print (a * 2)
    print ('+' * 50)
    print ("My Program")
    print ('+' * 50)

    a = "Life is Too short, You need Python"
    print (a[3])
    print (a[-0])
    print (a[-5])
    print (a[0:4])

    print(a[19:])
    print(a[:17])

    a = "20210704rainy"
    date = a[:8]
    weather = a[8:]
    print (date + " " + weather)

    a = "Pithon"
    ab = a[:1] + 'y' + a[2:]
    print (ab)

    a = "I eat %d apples" % 3
    print(a)

    a = "I eat %s apples" % "three"
    print(a)

    number = 10
    day = "three"

    a = "i ate %d aplles. so I was sick for %s days" % (number, day)
    print(a)

    a = "i ate %d%% percent" % 98
    print(a)

    a = "%10s" % "hi"
    print(a)

    a = "%0.4f" % 3.42134234
    print(a)

    a = "I eat {0} apples".format(3)
    print(a)

    a = "I eat {0} apples and {1} apples".format(3, "three")
    print(a)

    a = "I eat {number} apples and {name} apples".format(number=3, name="three")
    print(a)

    a = "I eat {number} apples and {0} apples".format("three", number=3)
    print(a)

    a = "{0:>10}".format("hi")
    print(a)

    a = "{0:^10}".format("hi")
    print(a)

    a = "{0:=^10}".format("hi")
    print(a)

    y = 3.5314213
    print("{0:0.4f}".format(y))

    y = 3.5314213
    print("{0:10.4f}".format(y))


    a = "hi"
    print(a.upper())
    print(a.lower())

    a = "Python is best choice"
    print(a.find("best"))
    a = ","
    print(a.join('abcd'))


    a = "   hi   "
    print(a)
    print(a.strip())
    print(a.lstrip())
    print(a.rstrip())

    a = "Life is too short"
    print(a.split())
    a = "a:b:c:d"
    print(a.split(":"))

    










