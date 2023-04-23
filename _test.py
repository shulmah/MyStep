# Программа получает на вход два числа
# Создать массив  A[n][m] и 
# заполнить спиралью

n,m= map(int, input('n,m: ').split())
matr=[]; c = 1
y, x = 0, -1
dy, dx = 0, 1 # step ^ step >

for i in range(n): # create [0]-matrix
    matr.append([0]*m)
    
for i in range(n): #print [0]-matrix
    for j in range(m):
        print(matr[i][j], end=' ')
    print()
   
while c <= n* m:
  if 0<=y+dy<n and 0<=x+dx<m and matr[y+dy][x+dx]==0:
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


# input().split() # целые числа как суб-строки, раздел-ные пробелом 
# n,m = map(int, input().split()) #  ввод 2-х чисел через пробел
# lst = list(map(int, input().split())) # ввод чисел через проб в списok
# lst = list(input().split()) # ввод str-чисел через пробел в список
# matr = [list(map(int, input().split())) for i in range(n)]

# if (w := 'walrus' in input().split()):
#     print('Нашли моржа')
# else:
#     print('Никаких моржей тут нет')

# w = map(str, input().split())
# if 'walrus' in w:
#     print('Нашли моржа')
# else:
#     print('Никаких моржей тут нет')

# ls = [[0,1,0,1,1],[1,1,0,0,1],[0,0,1,0,1],[1,0,0,0,1],[1,1,1,1,0]]
# for i in range(len(ls)):
#     for k in range(len(ls[i])):
#         print(ls[i][k],end=' ')
#     print()

#n, m = map(int, input().split())
#s = [list(map(str, input().split())) for i in range(n)]

n, m = 5 , 4
s = [   ['*', '*', '*', '.'],
        ['*', '*', '.', '.'],
        ['*', '.', '.', '.'],
        ['*', '.', '.', '.'],
        ['.', '.', '.', '*']]
print()
sk = [list(map(str,'-'.split()*m)) for i in range(n)]

print('sk=', so) 


