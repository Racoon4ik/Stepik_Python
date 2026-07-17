def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2
    
    # Сливаем два списка, пока один из них не закончится
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
            
    # Добавляем оставшиеся элементы
    if p1 < len(list1):
        result += list1[p1:]
    else:
        result += list2[p2:]
        
    return result

# Считываем количество списков
n = int(input())

# Накапливаем результат в total_list
total_list = []

for i in range(n):
    num = [int(q) for q in input().split()]
    # На каждом шаге объединяем уже накопленные числа с новой строкой
    total_list = quick_merge(total_list, num)

# Выводим итоговый список через пробел
print(*total_list)