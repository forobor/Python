'''
задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту, 
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Sample Input:
a3b4c2e10b1
Sample Output:
aaabbbbcceeeeeeeeeeb
'''

with open("dataset_3363_2.txt","r") as file:
	s=file.readline()
	s2=""
	for i in range(len(s)):
		#print(s[i])
		if s[i].isdigit():
			continue
		else:
			try:
				if s[i+2].isdigit():
					s2+=s[i]*int(s[i+1]+s[i+2])
				else:
					s2+=s[i]*int(s[i+1])
			except IndexError:
				break
	print(s2)
with open("ex.txt","w") as file:
	file.write(s2)