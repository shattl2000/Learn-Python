#Вывести последнюю букву в списке
word = 'Архангельск'
print ("Последняя буква:", word[-1])

#Вывести количество букв "а"" в слове
word = 'Архангельск'
result = word.count('А') + word.count('а')
print("Количество букв 'а':" , result)

#Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'АаЕеИиОоУуЫыЭэЮюЯя'
def count_vowels(word):
	num_vowels = 0
	for i in word:
		if i in vowels:
			num_vowels = num_vowels + 1
	return num_vowels
print("Количество гласных букв:", count_vowels(word))

#Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print("Количество слов в предложении:", len(sentence.split()))

#Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'