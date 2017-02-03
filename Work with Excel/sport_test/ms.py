#сборник python функций для расчета статистики для двумерных списков
import math
#среднее арифметическое
'''
передаваемые значения:
1. двумерный масив
2. столбец
'''
def average(tdarray,column):
	amount=0
	avg=0
	for i in range(len(tdarray)):
		if tdarray[i][column]=='':
			tdarray[i][column]=0
		amount+=tdarray[i][column]
	avg=amount/len(tdarray)
	return avg

#находим максимум 
'''
передаваемые значения:
1. двумерный масив
2. столбец
'''
def max_value(tdarray, column):
	max_num=0	
	for i in range(len(tdarray)):
		if tdarray[i][column]=='':
			tdarray[i][column]=0
		if int(tdarray[i][column])>max_num:
			max_num=tdarray[i][column]
	return max_num


#находим минимум
'''
передаваемые значения:
1. двумерный масив
2. столбец
3. максимальное число
'''
def min_value(tdarray, column, maximum):
	min_num=maximum
	for i in range(len(tdarray)):
		if tdarray[i][column]=='':
			tdarray[i][column]=0
		if int(tdarray[i][column])<min_num:
			min_num=tdarray[i][column]
	return min_num

#медиана
'''
передаваемые значения:
1. двумерный масив
2. столбец
'''
def median(tdarray,column):
	median=0
	data_array=[]	
	for i in range(len(tdarray)):
		if tdarray[i][column]=='':
			tdarray[i][column]=0
		data_array.append(int(tdarray[i][column]))
	data_array.sort()
	if len(data_array)%2!=0:
		median=data_array[math.floor(len(data_array)/2)]
	else:
		median=(data_array[int((len(data_array)/2))]+data_array[int((len(data_array)/2))-1])/2
	return median

#мода
'''
передаваемые значения:
1. двумерный масив
2. столбец
'''
def mode(tdarray,column):
	data_dict=dict()
	mode=0
	mode_count=0	
	for i in range(1,len(tdarray)):
		if tdarray[i][column]=='':
			tdarray[i][column]=0
		if tdarray[i][column] not in data_dict.keys():
			data_dict[tdarray[i][column]]=1
		else:
			data_dict[tdarray[i][column]]=data_dict[tdarray[i][column]]+1

	for key, value in data_dict.items():
		if value>mode_count:
			mode_count=value
			mode=key
	return mode