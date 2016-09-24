from parse_input import parse_input
import numpy as np

float_formatter = lambda x: "%.2f" % x 
np.set_printoptions(formatter={'float_kind':float_formatter})

a = 0.1
d = 25
P = parse_input()
lamdba_ = 100

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
lim = 10000
while (lim):
    lim -= 1

    r = np.dot(U, V)
    e = P - r
    
    for i in xrange(nu):
        for j in xrange(nv):
            U[i] = U[i] + a*(e[i][j]*V[:,j]-a*U[i])
            V[:,j] = V[:,j] + a*(e[i][j]*U[i]-a*V[:,j])

    print get_error(P, r)

