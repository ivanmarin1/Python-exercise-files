

square = []

for i in range(5):
    square.append(i*2)
# print(square)

a = "Hello", "Stupid", "Dumbass"
# print(len(a))
# print (a)

b = ["My", "new", "sequence"]
x, y, z = a
# print(x, y, z)

basket = {"apple", "orange", "apple", "pear", "orange"}
# print(basket)

pear = ()
# print(pear)

dic = {"kljuc3" : 2014, "kljuc2" : 2015, "kljuc1" : 2017, "kljuc4" : 2019}
print(list(dic))
print(sorted(dic))

dic["noviKljuc"] = 2020

print(list(dic))
print(sorted(dic))

tuples = "Hello", "enemy", "my", "old", "friend"
a1 = [1, 2, 3, 4, 5]
dic2 = {}
dic3 = {}

for i in range(5):
    dic2[tuples[i]] = a1[i]
    dic3 = dict([(tuples[i], a1[i])])

for k, v in enumerate(a):
    print(k, v)

