from collections import deque

def merge_and_sort_lists(list1, list2):
    # Создаем объединенный deque из двух списков
    combined_deque = deque(list1 + list2)
    
    # Сортируем deque и преобразуем его обратно в список
    return sorted(combined_deque)

# Пример использования
list1 = [1, 12, 34, 54]
list2 = [2, 11, 45, 232]

sorted_list = merge_and_sort_lists(list1, list2)
print(sorted_list)
