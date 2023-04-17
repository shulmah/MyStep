# Программа получает на вход два числа
# Создать массив  A[n][m] и 
# заполнить Змейкой

n,m= map(int, input().split())
s = []

for i in range(n):
    if i % 2 == 0:
        for j in range(i*m, i*m + m):
            s.append(j)
    else:
        for j in range((i+1)*m -1, i*m -1, -1):
            s.append(j)
for i in range(n):
    print(*s[(i*m): (i*m + m)])


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

print('sk=') # PRINT
for i in range(n):
    for j in range(m):
        print(sk[i][j],end=' ')
    print()

for i in range(n): # CHECK -->
    for j in range(m-1):
        if s[i][j]=='*':
            sk[i][j]='0'
            sk[i][j+1]='0'
for i in range(n): # CHECK <--
    for j in range(m-1,0,-1):
        if s[i][j]=='*':
            sk[i][j]='0'
            sk[i][j-1]='0'
for i in range(n-1): # CHECK DOWN
    for j in range(m):
        if s[i][j]=='*':
            sk[i][j]='0'
            sk[i+1][j]='0'
for i in range(n-1,0,-1): # CHECK UP
    for j in range(m):
        if s[i][j]=='*':
            sk[i][j]='0'
            sk[i-1][j]='0'

print('sk after=')
for i in range(n):   # PRINT
    for j in range(m):
        print(sk[i][j],end=' ')
    print()
print()

c=0
for i in range(n):
    for j in range(m):
        if sk[i][j]=='-':
            c += 1
print(c)
