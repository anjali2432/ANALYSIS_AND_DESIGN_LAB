a=int(input('Enter rows of prefactor:\t'))
b=int(input('Enter column of postfactor:\t'))
c=int(input('Enter column of postfactor:\t'))
A = [[0]*b]*a
B = [[0]*c]*b
C = [[0]*a]*c
for i in range(a):
  for j in range(b):
    A[i][j] = int(input('Enter value for prefactor:\t'))
for i in range(a):
  for j in range(b):
    B[i][j] = int(input('Enter value for postfactor:\t'))
for i in range(a):
  for j in range(b):
    C[i][j]=0
    for k in range(c):
      C[i][j]+=A[i][k]*B[k][j]
print(C)