age = int(input('Укажите Ваш возраст'))
print(age)

def check_activity(age):
    if age >= 3 and age <= 6:
        return "Детский сад"
    elif age >= 7 and age <= 17:
        return "Школа"
    elif age >= 18 and age <= 23:
        return "Университет"
    elif age >= 24 and age <= 60:
        return "Работа"
    else:
        return "Неактивный член общества"

society_function = check_activity(age)

print(society_function)


if __name__ == "__main__":
    main()