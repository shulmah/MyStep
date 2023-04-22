
# Программа получает на вход два числа
# Создать массив  A[n][m] и 
# заполнить Змейкой

n,m= map(int, input('n,m: ').split())
matr=[]; b=[]; s = []

for i in range(n): # create 0-matrix
    matr.append([0]*m)
    
for i in range(n): # print 0-matrix
   for j in range(m):
       print(matr[i][j], end=' ')
   print()
print()
c=0
for i in range(n): # added nums to matrix
   for j in range(m):
       c+=1
       if i ==0 and j < m: # add 0-str
           matr[i][j] = c
           
for i in range(n): # print num-matrix
   for j in range(m):
       print(matr[i][j], end=' ')
   print()               
               
           





