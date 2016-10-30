from parse_input import parse_input_test as parse_input
import numpy as np
import time

float_formatter = lambda x: "%.2f" % x 
np.set_printoptions(formatter={'float_kind':float_formatter})

d = 25
P,T = parse_input()
lamdba_ = 100

nv = np.shape(P)[1]
nu = np.shape(P)[0]

P_m = P.mean(axis=1)
P = (P.T - P_m).T
T = (T.T - P_m).T

def get_error(p,r):
    s = float(sum(sum((p-r*(p>1))**2)))
    n = sum(sum(p>1))
    return (s/n)**0.5

print "init"

u,s,v = np.linalg.svd(P)
print "svd done"
print np.shape(s)
t = np.count_nonzero(P)

for d in range(25,1000):
    P_dash = np.dot(u[:,:d] * s[:d], v[:d])
    print d,get_error(P,P_dash), get_error(T, P_dash)
