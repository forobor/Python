'''
Напишите программу, на вход которой подаётся квадратная матрица в виде последовательности строк, 
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов 
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''

a=[]
while True:
	s=[i for i in input().split()]
	if s!=["end"]:
		a.append(s)
	else:
		break

for i in range(len(a)):
	for j in range(len(a[i])):
		a[i][j]=int(a[i][j])

a2=[[0 for i in range(len(a[0]))]for i in range(len(a))]

width=len(a[0])-1
height=len(a)-1



for i in range(len(a)):
	for j in range(len(a[i])):
		if len(a)==1 and len(a[i])==1:
			a2[i][j]=a[i][j]*4
			break
		for di in range(-1,2,2):
			ai=i+di
			if 0<=ai<=height:
				a2[i][j]+=a[ai][j]
			elif ai<0:
				a2[i][j]+=a[height][j]
			elif ai>height:
				a2[i][j]+= a[0][j]

		for dj in range(-1,2,2):
			aj=j+dj
			if 0<=aj<=width:
				a2[i][j]+=a[i][aj]
			elif aj<0:
				a2[i][j]+=a[i][width]
			elif aj>width:
				a2[i][j]+=a[i][0]

for i in range(len(a2)):
	for j in range(len(a2[i])):
		print(a2[i][j],end=' ')
	print()


