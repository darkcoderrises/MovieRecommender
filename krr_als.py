from parse_input import parse_input_test as parse_input
import numpy as np
import time

float_formatter = lambda x: "%.2f" % x 
np.set_printoptions(formatter={'float_kind':float_formatter})

d = 25
P,T = parse_input()
P = P + T
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
lim = 10
while (lim):
    print lim
    lim -= 1

    U = np.linalg.solve(np.dot(V, V.T) + lamdba_ * np.eye(d), np.dot(V, P.T)).T 
    V = np.linalg.solve(np.dot(U.T, U) + lamdba_ * np.eye(d), np.dot(U.T, P)) 

def kernel(x,y):
    return np.exp(2*x.dot(y.T)-2)

P_ = U.dot(V)

for i in range(1,nu):
    print i,
    indexs = P[i] > 0
    if sum(indexs) == 0:
        continue
    X = V[:,indexs].T
    X = X / (((X**2).sum(axis=1))**0.5)[:,None]
    Y = P[i, indexs]
    try:
        Z = np.linalg.inv(kernel(X,X)+0.5).dot(Y)
        if abs(Z[0])>100:
            raise ValueError(' ')
    except:
        continue

    for j in range(1, nv):
        x = V[:,j]/(sum(V[:,j]**2)**0.5+0.1)
        y_ = kernel(x,X).dot(Z)
        P_[i,j] = y_

    print get_error(P,P_)
