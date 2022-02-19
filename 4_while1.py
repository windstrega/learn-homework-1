def hello_user():
 answer = True
 while answer:
    user = input('Как дела?')
    if user == 'Хорошо':
        answer = False
    else:
        answer = True
  


if __name__ == "__main__":
    hello_user()
