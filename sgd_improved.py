from parse_input import parse_input_test as parse_input
import numpy as np
import time
import warnings
warnings.filterwarnings("error")

float_formatter = lambda x: "%.2f" % x 
np.set_printoptions(formatter={'float_kind':float_formatter})

learning_rate = 0.001
regularization = 0.02
l2 = 0.05

d = 96
P,T = parse_input()

nv = np.shape(P)[1]
nu = np.shape(P)[0]

V = np.zeros([d, nv])
U = np.zeros([nu, d])
C = np.random.rand(nu,1)
D = np.random.rand(nv,1)

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

global_mean = float(sum(sum(P)))/sum(sum(P>1))

#ITERATING
rows,cols = P.nonzero()
lim = 10000
index = 0
while (lim):
    lim -= 1

    t1 = time.time()
    for u,i in zip(rows,cols):
        index += 1
        e = P[u,i] - C[u] - D[i] - np.dot(U[u,:],V[:,i])
        #print e
#        try:
        p_temp = learning_rate * (e * V[:,i] - regularization * U[u,:])
        V[:,i] += learning_rate * ( e * U[u,:] - regularization * V[:,i])
        U[u,:] += p_temp
#        except:
#            print "Warning", e, index

        c_temp = C[u]
        C[u] += learning_rate * (e - l2*(C[u]+D[i] - global_mean))
        D[i] += learning_rate * (e - l2*(c_temp+D[i] - global_mean))

    P_ = np.dot(U,V) 
    for i in range(nu):
        P_[i,:] += C[i]
    for j in range(nv):
        P_[:,j] += D[j]
    print time.time()-t1, get_error(P,P_), get_error(T,P_)
