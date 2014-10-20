
# Discrete Fourier Transform: only for the case when the signal length is a power of two.

from cmath import exp, pi, sqrt

x = 3           # change this to any nonnegative integer. 
N = 2**x
j = sqrt(-1)
data = []

# for the moment, let all x_n = 1 for all n and for each DFT sample.

for p in list(range(int(N))):
    sample_p = sum((exp(-j*2*pi/N))**(n*p) for n in list(range(int(N))))
    print(sample_p)

for p in list(range(int(N))):
    data.append([])
 
for p in list(range(int(N))):
    for n in list(range(int(N))):
        data[p].append((exp(-j*2*pi/N))**(n*p))
 
for p in list(range(int(N))):
    print("These entries are the coeffs of the terms in the %sth DFT sample: %s " % (p, data[p]))

 




 
 
 
 


