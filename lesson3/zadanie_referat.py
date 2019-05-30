#  Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
#  Подсчитайте количество слов в тексте
#  Замените точки в тексте на восклицательные знаки
#  Сохраните результат в файл referat2.txt

with open('referat.txt', 'r', encoding='utf-8') as text:
    content = text.read()
    print("Длина строки:", len(content))
    print("Количество слов:", len(content.split()))

with open('referat.txt', 'r', encoding='utf-8') as new_text:
	for line in new_text:
		line = line.replace('.', '!')
		with open('referat2.txt', 'a', encoding='utf-8') as f:
			f.write(line)

#with open('referat3.txt', 'r', encoding='utf-8') as f:
	#n_words = f.read()
	#print('количество слов в реферат2:', len(n_words.split()))