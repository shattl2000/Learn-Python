# Функция считает среднее значение, создан спсиок из словарей с оценками в школе,
# Выводит средний бал по каждому классу

def get_mid(a):
	for i in a:
		mid = sum(a) / len(a)
	return float(mid)

#b = [5, 5, 4, 2, 3, 3]
#get_mid(b)
#print (get_mid(b))

list_school = [
{'school_class': '4a', 'scores': [3, 4, 4, 5, 2, 2, 5]}, 
{'school_class': '4b', 'scores': [5, 3, 3, 5, 4, 5]},
{'school_class': '4c', 'scores': [5, 5, 4, 2, 3, 3, 4]},
]

for score_class in list_school:
	scores_mid = get_mid(score_class['scores'])
	print('Средняя оценка по классу', scores_mid)