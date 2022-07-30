import os
from pprint import pprint

# Задание 1

def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as file_object:
        cook_book = {}
        for line in file_object:
            dish_name = line.strip()
            ingredients_list = []
            ingredients_quantity = file_object.readline()
            for _ in range(int(ingredients_quantity)):
                ingredient_name, quantity, measure = file_object.readline().split(' | ')
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()})
            cook_book[dish_name] = ingredients_list
            file_object.readline()
    return cook_book

# pprint(get_cook_book(), sort_dicts=False, width=100)

# Задание 2

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    shop_dict = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for recipe in cook_book[dish]:
                if recipe['ingredient_name'] in shop_dict:
                    shop_dict[recipe['ingredient_name']]['quantity'] += recipe['quantity'] * person_count
                else:
                    shop_dict[recipe['ingredient_name']] = {'measure': recipe['measure'], 'quantity': (recipe['quantity'] * person_count)}
        else:
            error = 'Ошибка: введённого Вами блюда нет в кулинарной книге'
            return error
    return shop_dict

# pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Запеченный картофель'], 3), sort_dicts=False)
# pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2), sort_dicts=False) 

# Задание 3

def get_path_to_texts():
    TEXTS_DIR = 'texts'
    full_path_to_texts = os.path.join(os.getcwd(), TEXTS_DIR)
    return full_path_to_texts

def get_path_to_sorted_file():
    SORTED_FILE = 'sorted_texts.txt'
    sorted_full_path = os.path.join(os.getcwd(), SORTED_FILE)
    return sorted_full_path

def get_texts_list():
    texts_list = os.listdir(get_path_to_texts()) 
    return texts_list

def get_sorted_texts():
    all_texts = {}
    for file in get_texts_list():
        file_path = os.path.join(get_path_to_texts(), file)
        with open(file_path, 'r', encoding = 'utf-8') as file_to_read:
            list_of_strings = []
            for line in file_to_read:
                list_of_strings.append(line.strip())
            text = '\n'.join(list_of_strings)
        all_texts[len(list_of_strings)] = {'name': file, 'length': str(len(list_of_strings)), 'text': text}
    return all_texts

def write_down_sorted_texts():
    all_texts = get_sorted_texts()
    sorted_len = sorted(all_texts.keys())
    with open(get_path_to_sorted_file(), 'w', encoding = 'utf-8') as file_to_write:
        for i in sorted_len:
            file_to_write.write(all_texts[i]['name'] + '\n' + all_texts[i]['length'] + '\n' + all_texts[i]['text'] + '\n')
    return 'Sorted texts were written down.'

# print(write_down_sorted_texts())