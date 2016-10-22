import matplotlib.pyplot as plt

l = []
b = []

data = open('als/data').read().split('\n')[:-1]

for i in data:
    print i.split(" ")
    ll, bb = map(float, i.split(" "))
    b.append(bb)
    
    if len(l)>0:
        l.append(ll+l[-1])
    else:
        l.append(ll)

plt.plot(l,b)
plt.show()
