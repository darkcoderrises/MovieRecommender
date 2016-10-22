from parse_input import parse_input
import numpy as np
import time

float_formatter = lambda x: "%.2f" % x 
np.set_printoptions(formatter={'float_kind':float_formatter})

learning_rate = 0.01
regularization = 0.01
d = 25
P = parse_input()

nv = np.shape(P)[1]
nu = np.shape(P)[0]

V = np.zeros([d, nv])
U = np.zeros([nu, d])


def get_error(p,r):
    s = float(sum(sum((p-r*(p>=1))**2)))
    n = sum(sum(p>1))
    return (s/n)**0.5

#INITIALIZATION
print "initialization"
for i in range(1, nv):
    V[0, i] = sum(P[:,i])/nu #Movie average rating
    for j in range(1, d):
        V[j, i] = np.random.random()

#ITERATING
rows,cols = P.nonzero()
lim = 10000
while (lim):
    lim -= 1

    t1 = time.time()
    for u,i in zip(rows,cols):
        e = P[u,i] - np.dot(U[u,:],V[:,i])
        p_temp = learning_rate * (e * V[:,i] - regularization * U[u,:])

        V[:,i] += learning_rate * ( e * U[u,:] - regularization * V[:,i])
        U[u,:] += p_temp


    print time.time()-t1,get_error(P, np.dot(U,V))

