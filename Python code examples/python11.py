'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча 
и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2

Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
'''
n=int(input())
tab=[]
for i in range(n):
	tab.append(input().split(';'))
vivod=dict()
win=0
lose=0
draw=0
score=0
count=0
for i in range(len(tab)):
	if tab[i][0] not in vivod.keys():
		for j in range(len(tab)):
			if tab[i][0]==tab[j][0]:
				count+=1
				if tab[j][1]>tab[j][3]:
					win+=1
					score+=3
				elif tab[j][1]<tab[j][3]:
					lose+=1
				elif tab[j][1]==tab[j][3]:
					draw+=1
					score+=1
			elif tab[i][0]==tab[j][2]:
				count+=1
				if tab[j][1]>tab[j][3]:
					lose+=1
				elif tab[j][1]<tab[j][3]:
					win+=1
					score+=3
				elif tab[j][1]==tab[j][3]:
					draw+=1
					score+=1				
		vivod[tab[i][0]]=[count,win,draw,lose,score]
		count=0
		win=0
		lose=0
		draw=0
		score=0	


	if tab[i][2] not in vivod.keys():
		for j in range(len(tab)):
			if tab[i][2]==tab[j][2]:
				count+=1
				if tab[j][3]>tab[j][1]:
					win+=1
					score+=3
				elif tab[j][3]<tab[j][1]:
					lose+=1
				elif tab[j][3]==tab[j][1]:
					draw+=1
					score+=1
			if tab[i][2]==tab[j][0]:
				count+=1
				if tab[j][1]>tab[j][3]:
					win+=1
					score+=3
				elif tab[j][1]<tab[j][3]:
					lose+=1
				elif tab[j][1]==tab[j][3]:
					draw+=1
					score+=1
		vivod[tab[i][2]]=[count,win,draw,lose,score]
		count=0
		win=0
		lose=0
		draw=0
		score=0	


for k,v in vivod.items():
	print(k + ":",end="")
	for z in v:
		print(z, end=" ")
	print()