import matplotlib.pyplot as plt

l = []
b = []

data = open('knn/data').read().split('\n')[:-1]

for i in data:
    print i.split(" ")
    ll, bb, c = map(float, i.split(" "))
    b.append(bb)
    
    l.append(ll)

plt.plot(l,b)
plt.show()
