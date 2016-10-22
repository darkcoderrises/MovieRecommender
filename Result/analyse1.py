import matplotlib.pyplot as plt

n = ['als/data', 'sgd/data']

for k in n:
    l = []
    b = []
    data = open(k).read().split('\n')[:-1]

    for i in data:
        ll, bb = map(float, i.split(" "))
        b.append(bb)
        
        if len(l)>0:
            l.append(ll+l[-1])
        else:
            l.append(ll)

    plt.plot(l,b)
plt.show()
