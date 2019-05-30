#Запись в файл

#with open ('text.txt', 'a', encoding='utf-8') as f:
#	f.write('Добавили вторую строку\n')

#Чтение из файла

with open ('text.txt', 'r', encoding='utf-8') as f:
	for line in f:
		line = line.upper()
		line = line.replace('\n', '')
		print(line)