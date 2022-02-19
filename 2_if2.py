def my_strings(str1, str2):

    if type(str1) != str or type(str2) != str:
        return 0
    elif len(str1) == len(str2):
        return 1
    elif len(str1) > len(str2) and str2 != "learn":
        return 2
    elif len(str1) != len(str2) and str2 == "learn":
        return 3
    
str1 = "коробка"
str2 = "learn"
    
print(my_strings(str1, str2))

str1 = "корова"
str2 = "кот"

print(my_strings(str1, str2))

str1 = 5
str2 = "кот"

print(my_strings(str1, str2))

str1 = "машина"
str2 = "корова"

print(my_strings(str1, str2))
  

if __name__ == "__main__":
    main()
