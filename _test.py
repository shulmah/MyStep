<<<<<<< HEAD
<<<<<<< HEAD
# Программа получает на вход два числа
# Создать массив  A[n][m] и 
# заполнить спиралью

n,m= map(int, input('n,m: ').split())
matr=[]; c = 1
y, x = 0, -1  # point-start
dy, dx = 0, 1 # step ^ step >

for i in range(n): # create [0]-matrix
    matr.append([0]*m)
    
for i in range(n): #print [0]-matrix
    for j in range(m):
        print(matr[i][j], end=' ')
    print()
   
while c <= n* m:
  if y+dy in range(n) and x+dx in range(m) and matr[y+dy][x+dx]==0:
    y += dy
    x += dx
    matr[y][x] = c
    c += 1
  elif dx == 1:
    dx = 0
    dy = 1
  elif dy == 1:
    dy = 0
    dx = -1
  elif dx == -1:
    dx = 0
    dy = -1
  elif dy == -1:
    dy = 0
    dx = 1

print() 
for i in range(n): #print n*m-matrix
    for j in range(m):
        print(matr[i][j], end=' ')
    print()
               
=======

oauth_token: gho_u9gvfeURy6zaI9KaiEqlWKiBvC0QCr2qJwc    user: shulmah
=======
# Создать массив  A[n][n]
# заполнить спиралью

n =int(input('n: '))
matr=[]
y,x = 0,-1 # start-point
dy = 0 # -1, 0, 1
dx = 1 # -1, 0, 1

for i in range(n): # create 0-matrix
    matr.append([0]*n)
>>>>>>> brhash

c = 1
while c <= n**2:
    if y + dy in range(n)and x + dx in range(n) and matr[y + dy][x + dx] == 0:
        y += dy
        x += dx
        matr[y][x] = c
        c += 1
    else:
        if dx == 1:
            dx = 0
            dy = 1
        elif dy == 1:
            dy = 0
            dx = -1
        elif dx == -1:
            dx = 0
            dy = -1
        elif dy == -1:
            dy = 0
            dx = 1

<<<<<<< HEAD

>>>>>>> fix-code
=======
for i in range(n): # print 0-matrix
   for j in range(n):
       print(matr[i][j], end=' ')
   print()
print()


# n, m = 5 , 4
# s = [   ['*', '*', '*', '.'],
#         ['*', '*', '.', '.'],
#         ['*', '.', '.', '.'],
#         ['*', '.', '.', '.'],
#         ['.', '.', '.', '*']]
# print()
# sk = [list(map(str,'-'.split()*m)) for i in range(n)]
#
# print('sk=', so)


>>>>>>> brhash
