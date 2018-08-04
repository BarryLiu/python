
l = ["集合%d"%i for i in range(1,10,2)]
print(l)

t = ("集合%d"%i for i in range(1,10,2))
print(t.__next__())
print(t.__next__())


name=['alex_sb','sfafafafa']
res=filter(lambda x:not x.endswith('sb'),name)
print(res)
print(list(res))


# lambda
g = lambda x:x*2
print(g(3))

# random.choice
import random
a = random.choice([1,5,2,6])
print(a)


# callable()


