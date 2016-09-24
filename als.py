from parse_input import parse_input
import numpy as np

float_formatter = lambda x: "%.2f" % x 
np.set_printoptions(formatter={'float_kind':float_formatter})

d = 25
P = parse_input()
lamdba_ = 100

nv = np.shape(P)[1]
nu = np.shape(P)[0]

V = np.zeros([d, nv])
U = np.zeros([nu, d])


def get_error(p,r):
    s = float(sum(sum((p-r*(p>1))**2)))
    n = sum(sum(p>1))
    return (s/n)**0.5

#INITIALIZATION
print "initialization"
for i in range(1, nv):
    V[0, i] = sum(P[:,i])/nu #Movie average rating
    for j in range(1, d):
        V[j, i] = np.random.random()

#ITERATING
lim = 1000
while (lim):
    lim -= 1

    U = np.linalg.solve(np.dot(V, V.T) + lamdba_ * np.eye(d), np.dot(V, P.T)).T 
    V = np.linalg.solve(np.dot(U.T, U) + lamdba_ * np.eye(d), np.dot(U.T, P)) 

    r = np.dot(U, V)
    print get_error(P, r)

