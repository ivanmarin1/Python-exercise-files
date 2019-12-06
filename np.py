import numpy as np

a = np.array([1, 2, 3, 4, 5])

#print(a.ndim)
#print(a.data)

b = np.arange(6)
#print(b)

c = np.arange(12).reshape(4, 3)
#print(c)

c = c * 2
print(c)

#print(c.sum(axis=0))

#print(c[:3, :2])

#for x in c.flat:
#    print(x)

d = c > 4
print(d)

e = np.random.random(5)
print(e)

x = np.arange(10)
x.shape = (2, 5)
print(x[1, 2])

