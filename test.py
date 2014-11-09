"""
Testing concept of passing object reference by value
Everything is pass by value but the values are object's reference
"""
import random
import copy


def testMem():
    a = [[1], [2]]

    for i in a:
        i = []
        # Expect no change to a as everything are passed by value
        # This means that i recieves the address of [1] then it is
        # given the address of []. So nothing happens to a.

    print(a)

    for i in a:
        i.append(2)
        # Now the output will be dffferent because i refers to [1]
        # and that append will be working on [1]

    print(a)


def changeFirst(l):
    l[0] = 9999


def testChange():
    b = [i for i in range(10)]

    changeFirst(b)
    changeFirst(b[2:])
    print(b)


def testShuffle():
    a = [i for i in range(10)]
    res = []
    for i in range(100):
        random.shuffle(a)
        res.append(copy.copy(a))
    # Need to do a copy as it will just append the reference to a
    # When it prints, it will all be the same value
    print(res)


class test:
    cnt = 0

    def __init__(self, name):
        self.name = name
        self.idx = test.cnt
        print("{} used the constructor in test.".format(name))
        test.cnt += 1

    def shout(self):
        print("Name is {}!".format(self.name))


class inTest(test):

    def __init__(self, name):
        """If defined, will not use constructor of base class"""
        print("{} used the constructor in inTest".format(name))
        self.idx = test.cnt
        self.name = name
        test.cnt += 1

    def shout(self, num):
        print("Name is {}!".format(self.name) * 2)


def testClass():
    a = test("hello")
    b = inTest("there")
    print(a.idx, b.idx)
    a.shout()
    # Explicitly calling the base class method
    # and passing the instance of subclass
    test.shout(b)
    b.shout(2)

    # This is the closest to type cast that you can with python
    # However, this is permenant and would lose your access to derived class
    b.__class__ = test
    b.shout()
    b.shout(2)

testClass()
