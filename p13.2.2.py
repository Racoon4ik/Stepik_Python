# объявление функции
def print_case_counts(s):
    # объявление функции
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    print(f"Букв в верхнем регистре: {upper_count}")
    print(f"Букв в нижнем регистре: {lower_count}")
# считываем данные
s = input()

# вызываем функцию
print_case_counts(s)