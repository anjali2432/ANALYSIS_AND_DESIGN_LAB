def minGrid(mat,i,j,m,n,num):
  val = mat[i][j]   
  a=i+1
  b=j+1
  c=i-1
  d=j-1
  if a >= m :
    a = val
  else:
    a = mat[a][j]
  if b >= n :
    b = val
  else:
    b = mat[i][b]
  if c < 0 :
    c = val
  else:
    c = mat[c][j]
  if d < 0 :
    d = val
  else:
    d = mat[i][d]
  min_val = min([a,b,c,d,val])
  if min_val == val :
    num += 1
    return {num:[i,j,val]}
  else :
    return {0:[-1,-1,-1]}
def allMinGrid(mat,m,n):
  minimas = dict({0:[-1,-1,-1]})
  count = 0
  for i in range(m):
    for j in range(n):
      minimas.update(minGrid(mat,i,j,m,n,count))
      if (count+1) in minimas.keys() :
        count += 1
  minimas.pop(0)
  return minimas
row = int(input('Enter required number of rows\t'))
col = int(input('Enter required number of columns\t'))
IPMatrix = []
print('Enter values\t')
for i in range(row) :
  a = []
  for j in range(col) :
    a.append(int(input()))
  IPMatrix.append(a)
result = allMinGrid(IPMatrix,row,col)
print(IPMatrix)
print(result)