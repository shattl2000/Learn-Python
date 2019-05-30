#Программа все время просит задать вопрос и дает ответы из словаря пока не написать "отстань", 
#try: except: перехватывает ошибку KeyboardInterrupt

question_answer = {"как дела?": "Хорошо!", "что делаешь?": "Программирую", "когда закончишь?": "Не знаю"}

try:
	while True:
		question_user = input('Задайте мне вопрос: ')
		if question_user in question_answer:
			print(question_answer[question_user])
		elif question_user == 'отстань':
				print('Пока!')
				break
		else: 
			print('Спроси еще что-то')

except KeyboardInterrupt:
	print('Пока')