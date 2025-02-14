"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""



questions_and_answers = {
    'Как дела?': 'Жесть', 
    'Что делаешь?': 'Копирую код', 
    'В чём проблема?': 'Ничего не понимаю', 
    'Будешь чай?': 'Давай'
    }
def ask_user(questions_and_answers):
    inputisactive = True
    while inputisactive:
        question = input("Есть вопросы?")
        if question in questions_and_answers.keys():
            print(questions_and_answers[question])
        else:
            continue
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
