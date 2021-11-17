import numpy as np
x=[40,10,20,5,45,50,65,90,35,25]
y=len(x)
z=x[:]
z.sort()
w=x[:]
w.sort(reverse=True)
v=x.count(x[0])
peak=[]
for i in range(y):
  if (v==y):
    print(" Here v is the list for checking the condition weather the list contains same elements or not")
    peak.append(x[0])
    break
  if (z==x):
    print(" Here z is the list for checking the ascending order condition")
    peak.append(z[-1])
    break
  if (w==x):
    print(" Here w is the list for checking the descending order condition")
    peak.append(w[0])
    break
  if (x[i-1]<x[i] and x[i]>x[i+1]):
    peak.append(x[i])
print("the peak values are:",peak)
print("square root of the values are:",np.sqrt(peak))
