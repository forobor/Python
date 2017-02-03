'''
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
 и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. 
 Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
'''

with open("dataset_3363_3.txt",'r') as file:
    s=file.read().lower().split()
    print(s)
    s2=""
    c=0
    for i in s:
        if s.count(i)>c:
            s2=i
            c=s.count(i)
        elif s.count(i)==c:
            if s2> i:
               s2=i 
    print(s2,c)
    
with open("ex.txt",'w') as file:
    file.write(s2 + " " + str(c))
    
