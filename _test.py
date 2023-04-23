# Создать массив  A[n][n]
# заполнить спиралью

n =int(input('n: '))
matr=[]
y,x = 0,-1 # start-point
dy = 0 # -1, 0, 1
dx = 1 # -1, 0, 1

for i in range(n): # create 0-matrix
    matr.append([0]*n)

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


