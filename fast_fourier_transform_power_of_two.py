
# this code verifies the computational time for DFT using FFT algorithm by factorizing the transition matrix  
# when the signal length is a power of two. 

# plug in x in N = 2^x. The code aims to produce transition matrices, each of which has computation time N.  
# This code will ultimately verify that FFT computes DFT from a configuration space to the frquency space 
# asymptotically in O(N Log_2(N))-time.  


 
from math import atan
from cmath import exp, pi, sqrt, phase
 

x = 2
N = 2**x
j = sqrt(-1)
data = []  # in cartesian 
data_polar = []  # in polar  

for p in list(range(int(N))):
    data.append([])
    data_polar.append([])

cob_1_even = []
cob_1_odd = [] 

 
 
for p in list(range(int(N))):
    for n in list(range(int(N))):
        data[p].append((exp(-j*2*pi/N))**(n*p))
        data_polar[p].append([abs((exp(-j*2*pi/N))**(n*p)),phase((exp(-j*2*pi/N))**(n*p))]) 

for p in list(range(int(N))): 
    print("These entries are the coeffs of the terms in the %sth DFT sample: %s " % (p, data_polar[p]))
 
for p in list(range(int(N))):
    for j in list(range(int(N/2)-1)):
        cob_1_even.append([data_polar[p][j], data_polar[p][int(j+(int(N)/2))]])
        cob_1_odd.append([data_polar[p][j+1], data_polar[p][int(j+(int(N)/2)+1)]]) 

 
for i in list(range(int(N))):
    if float(cob_1_odd[i][0][1]) !=0:
        cob_1_odd[i][1][1] = cob_1_odd[i][1][1] - cob_1_odd[i][0][1]
        cob_1_odd[i][0][1] = 0.0  
 
 

print("\n") 
print(cob_1_even)
print("\n") 
print(cob_1_odd)
