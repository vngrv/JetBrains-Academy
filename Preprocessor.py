n1, m1 = input().split()
n1 = int(n1)
m1 = int(m1)

a1 = []
a2 = []

for i in range(n1):
    a1.append(list(map(int, input().split())))

n2, m2 = input().split()
n2 = int(n2)
m2 = int(m2)

for i in range(n2):
    a2.append(list(map(int, input().split())))

for i in range(len(a1)):
    for j in range(len(a1[i])):
        a1[i][j] = a1[i][j] + a2[i][j]

if(n1 != n2 and m1 != m2):
    print("ERROR")
else:
    for i in range(len(a1)):
        print(*a1[i])

