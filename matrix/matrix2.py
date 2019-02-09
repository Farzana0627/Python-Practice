import numpy as np
from array import *
from numpy import * 

X = np.random.uniform(size=(10,3))
n,m = X.shape # for generality
X0 = np.ones((n,2))
Xnew = np.hstack((X,X0))

#print(X)
#print(X0)
#print(Xnew)



m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
#m_c = insert(m,[5],[[1,0],[2,1],[3,2],[4,3],[5,4],[6,5],[7,6]],2)
print(m)