"""
Testing concept of passing object reference by value
Everything is pass by value but the values are object's reference
"""

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

b = [i for i in range(10)]

changeFirst(b)
changeFirst(b[2:])
print(b)


for i in range(0, -1, -1):
    print(i)
