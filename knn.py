from parse_input import parse_input_test as parse_input
import numpy as np
import time

float_formatter = lambda x: "%.2f" % x 
np.set_printoptions(formatter={'float_kind':float_formatter})

k = 10
P,T = parse_input()

nv = np.shape(P)[1]
nu = np.shape(P)[0]

def get_error(p,r):
    s = float(sum(sum((p-r*(p>1))**2)))
    n = sum(sum(p>1))
    return (s/n)**0.5

print "init"

p_mean = sum(P)/(sum(P>0)+0.0000001)
P_ = P - p_mean
P_normalized = P_/(sum(P_**2)**0.5+0.0000001)

sim_matrix = P_normalized.T.dot(P_normalized)
ans = np.zeros([nu,nv])

for j in range(1,nv):
	indexs = sim_matrix[:,j].argsort()[-(k+1):-1][::-1]
	n = P[:,indexs]
	l = sim_matrix[j,indexs]

	ans[:,j] = sum((n*l).T)/(sum(abs(l))+0.0000001)
	if j%100==0:
		print j, get_error(P, ans), get_error(T, ans)
print nv,get_error(P, ans), get_error(T, ans)