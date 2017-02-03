'''
Выведите таблицу размером nxnxn, заполненную числами от 1 до n**2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке
'''
n=int(input())
n1=n**2
k=0
a=[[0 for i in range(n)]for j in range(n)]
while n!=0:
	if n**2 in a:
		break
	else:
		for j in range(k,n): #1, 1
			if k==0 and j==0:
				a[k][j]=1
			else:
				a[k][j]=a[k][j-1]+1 #1, 1 = 1

		for i in range(1,n): #1, 1
			if a[i+k][n-1] ==0:
				a[i+k][n-1]=a[i+k-1][n-1]+1 #2, 1			
			else:
				break
		
		for j in range(n-2,-1,-1):
			if a[n-1][j] ==0:
				a[n-1][j]=a[n-1][j+1]+1
			else:
				break
			
		
		for i in range(n-2,k,-1):
			if a[i][k] ==0:
				a[i][k]=a[i+1][k]+1
			else:
				break
		
		k+=1
		n-=1


for i in range(len(a)):
	for j in range(len(a[i])):
		print(a[i][j],end=' ')
	print()