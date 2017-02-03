import xlrd, xlwt
import ms

#форматирование масива по типу
def format_array(name,big_array):
	array=[]
	for i in range(len(big_array)):
		if big_array[i][0]==name:
			array.append(big_array[i])
	return array




#открытие файла
book=xlrd.open_workbook('docs/dataset.xls',formatting_info=True)
#выбираем лист
sheet=book.sheet_by_index(0)

#получаем список значений всех ячеек таблицы
info=[sheet.row_values(rownum) for rownum in range(sheet.nrows)]

#создаем массив из необходимой информации
datalist=info[1:len(info)]

#создадим новый файл excel для записи
wb=xlwt.Workbook()
ws=wb.add_sheet('Test')

#заполним ячейки excel
ws.write(0,0,"Общая статистика")
ws.write(2,0,"Cреднее")
ws.write(3,0,"Макс")
ws.write(4,0,"Мин")
ws.write(5,0,"Медиана")
ws.write(6,0,"Мода")
z=1
for c in (info[0][5:19]):
	ws.write(1,z,c)
	z+=1

#находим среднее значение
z=1
for j in range(5,len(info[1])) :
	ws.write(2,z,ms.average(datalist,j))
	z+=1	

#находим максимум 
z=1
for j in range(5,len(info[1])) :	
	ws.write(3,z,ms.max_value(datalist,j))
	z+=1	

#наибольшее число в массиве
maximum=0
for j in range(5,len(info[1])) :	
	for i in range(1,len(info)):
			if int(info[i][j])>maximum:
				maximum=info[i][j]

#находим минимум
z=1
for j in range(5,len(info[1])) :	
	ws.write(4,z,ms.min_value(datalist,j,maximum))
	z+=1	

#медиана
z=1
for j in range(5,len(info[1])) :	
	ws.write(5,z,ms.median(datalist,j))
	z+=1

#мода
z=1
for j in range(5,len(info[1])) :	
	ws.write(6,z,ms.mode(datalist,j))
	z+=1


#------------------------------------------------------------------------------------------------------------------------------------------

#расчет статистики для каждого из типов

ws.write(8,0,"Статистика каждого типа")
ws.write(10,0,"Link")
ws.write(12,0,"Cреднее")
ws.write(13,0,"Макс")
ws.write(14,0,"Мин")
ws.write(15,0,"Медиана")
ws.write(16,0,"Мода")
z=2
for c in (info[0][6:19]):
	ws.write(11,z,c)
	z+=1

#создание массива для Link
link_arr=format_array('Link',datalist)
ws.write(10,1, "Totals posts:")
ws.write(10,2,len(link_arr))

#находим среднее значение для Link
z=2
for j in range(6,len(link_arr[1])) :
	ws.write(12,z,ms.average(link_arr,j))
	z+=1	

#находим максимум  для Link
z=2
for j in range(6,len(link_arr[1])) :	
	ws.write(13,z,ms.max_value(link_arr,j))
	z+=1	

#наибольшее число в массиве для Link
maximum=0
for j in range(6,len(link_arr[1])) :	
	for i in range(1,len(link_arr)):
			if int(link_arr[i][j])>maximum:
				maximum=link_arr[i][j]

#находим минимум для Link
z=2
for j in range(6,len(link_arr[1])) :	
	ws.write(14,z,ms.min_value(link_arr,j,maximum))
	z+=1	

#медиана для Link
z=2
for j in range(6,len(link_arr[1])) :	
	ws.write(15,z,ms.median(link_arr,j))
	z+=1

#мода для Link
z=2
for j in range(6,len(link_arr[1])) :	
	ws.write(16,z,ms.mode(link_arr,j))
	z+=1

#------------------------------------------------------------------------

ws.write(18,0,"Photo")
ws.write(20,0,"Cреднее")
ws.write(21,0,"Макс")
ws.write(22,0,"Мин")
ws.write(23,0,"Медиана")
ws.write(24,0,"Мода")
z=2
for c in (info[0][6:19]):
	ws.write(19,z,c)
	z+=1

#создание массива для Photo
photo_arr=format_array('Photo',datalist)
ws.write(18,1, "Totals posts:")
ws.write(18,2,len(photo_arr))

#находим среднее значение для Photo
z=2
for j in range(6,len(photo_arr[1])) :
	ws.write(20,z,ms.average(photo_arr,j))
	z+=1	

#находим максимум  для Photo
z=2
for j in range(6,len(photo_arr[1])) :	
	ws.write(21,z,ms.max_value(photo_arr,j))
	z+=1	

#наибольшее число в массиве для Photo
maximum=0
for j in range(6,len(photo_arr[1])) :	
	for i in range(1,len(photo_arr)):
			if int(photo_arr[i][j])>maximum:
				maximum=photo_arr[i][j]

#находим минимум для Photo
z=2
for j in range(6,len(photo_arr[1])) :	
	ws.write(22,z,ms.min_value(photo_arr,j,maximum))
	z+=1	

#медиана для Photo
z=2
for j in range(6,len(photo_arr[1])) :	
	ws.write(23,z,ms.median(photo_arr,j))
	z+=1

#мода для Photo
z=2
for j in range(6,len(photo_arr[1])) :	
	ws.write(24,z,ms.mode(photo_arr,j))
	z+=1

#------------------------------------------------------------------------

ws.write(26,0,"Status")
ws.write(28,0,"Cреднее")
ws.write(29,0,"Макс")
ws.write(30,0,"Мин")
ws.write(31,0,"Медиана")
ws.write(32,0,"Мода")
z=2
for c in (info[0][6:19]):
	ws.write(27,z,c)
	z+=1

#создание массива для Status
status_arr=format_array('Status',datalist)
ws.write(26,1, "Totals posts:")
ws.write(26,2,len(status_arr))

#находим среднее значение для Status
z=2
for j in range(6,len(status_arr[1])) :
	ws.write(28,z,ms.average(status_arr,j))
	z+=1	

#находим максимум  для Status
z=2
for j in range(6,len(status_arr[1])) :	
	ws.write(29,z,ms.max_value(status_arr,j))
	z+=1	

#наибольшее число в массиве для Status
maximum=0
for j in range(6,len(status_arr[1])) :	
	for i in range(1,len(status_arr)):
			if int(status_arr[i][j])>maximum:
				maximum=status_arr[i][j]

#находим минимум для Status
z=2
for j in range(6,len(status_arr[1])) :	
	ws.write(30,z,ms.min_value(status_arr,j,maximum))
	z+=1	

#медиана для Status
z=2
for j in range(6,len(status_arr[1])) :	
	ws.write(31,z,ms.median(status_arr,j))
	z+=1

#мода для Status
z=2
for j in range(6,len(status_arr[1])) :	
	ws.write(32,z,ms.mode(status_arr,j))
	z+=1

#------------------------------------------------------------------------

ws.write(34,0,"Video")
ws.write(36,0,"Cреднее")
ws.write(37,0,"Макс")
ws.write(38,0,"Мин")
ws.write(39,0,"Медиана")
ws.write(40,0,"Мода")
z=2
for c in (info[0][6:19]):
	ws.write(35,z,c)
	z+=1

#создание массива для Video
video_arr=format_array('Video',datalist)
ws.write(34,1, "Totals posts:")
ws.write(34,2,len(video_arr))

#находим среднее значение для Video
z=2
for j in range(6,len(video_arr[1])) :
	ws.write(36,z,ms.average(video_arr,j))
	z+=1	

#находим максимум  для Video
z=2
for j in range(6,len(video_arr[1])) :	
	ws.write(37,z,ms.max_value(video_arr,j))
	z+=1	

#наибольшее число в массиве для Video
maximum=0
for j in range(6,len(video_arr[1])) :	
	for i in range(1,len(video_arr)):
			if int(video_arr[i][j])>maximum:
				maximum=video_arr[i][j]

#находим минимум для Video
z=2
for j in range(6,len(video_arr[1])) :	
	ws.write(38,z,ms.min_value(video_arr,j,maximum))
	z+=1	

#медиана для Video
z=2
for j in range(6,len(video_arr[1])) :	
	ws.write(39,z,ms.median(video_arr,j))
	z+=1

#мода для Video
z=2
for j in range(6,len(video_arr[1])) :	
	ws.write(40,z,ms.mode(video_arr,j))
	z+=1

#------------------------------------------------------------------------

#Мода для типа, категории, дня, часа
ws.write(42,0,"Статистика для Type, Category, Month, Weekday, Hour")

z=1
for c in (info[0][:5]):
	ws.write(43,z,c)
	z+=1

ws.write(44,0,"Среднее")
ws.write(45,0,"Медиана")
ws.write(46,0,"Мода")

print(datalist[1][3:5])
#среднее
z=4
for j in range(3,5) :	
	ws.write(44,z,ms.average(datalist,j))
	z+=1

#медиана
z=4
for j in range(3,5) :	
	ws.write(45,z,ms.median(datalist,j))
	z+=1


#мода
z=1
for j in range(len(datalist[1][:5])) :	
	ws.write(46,z,ms.mode(datalist,j))
	z+=1



wb.save('docs/analys.xls')
