import os
from pprint import pprint

# Задание 1

with open('recipes.txt', encoding='utf-8') as file_object:
    cook_book = {}
    for line in file_object:
        dish_name = line.strip()
        ingredients_list = []
        ingredients_quantity = file_object.readline()
        for item in range(int(ingredients_quantity)):
            ingredients_dict = {}
            ingredient_name, quantity, measure = file_object.readline().split(' | ')
            ingredients_dict['ingredient_name'] = ingredient_name
            ingredients_dict['quantity'] = int(quantity)
            ingredients_dict['measure'] = measure.strip()
            ingredients_list.append(ingredients_dict)
        cook_book[dish_name] = ingredients_list
        file_object.readline()

#pprint(cook_book, sort_dicts=False, width=100)

# Задание 2

def get_shop_list_by_dishes(dishes, person_count):
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

#pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Запеченный картофель'], 3), sort_dicts=False)
#pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2), sort_dicts=False) 

# Задание 3

CURRENT_DIR = os.getcwd()
TEXTS_DIR = 'texts'
SORTED_FILE = 'sorted_texts.txt'
full_path_to_texts = os.path.join(CURRENT_DIR, TEXTS_DIR)
sorted_full_path = os.path.join(CURRENT_DIR, SORTED_FILE)
texts_list = os.listdir(full_path_to_texts) 
all_texts = {}

for file in texts_list:
    file_path = os.path.join(CURRENT_DIR, TEXTS_DIR, file)
    with open(file_path, 'r', encoding = 'utf-8') as file_to_read:
        list_of_strings = []
        for line in file_to_read:
            list_of_strings.append(line.strip())
        text = '\n'.join(list_of_strings)
    all_texts[len(list_of_strings)] = {'name': file, 'length': str(len(list_of_strings)), 'text': text}
    sorted_len = sorted(all_texts.keys())

with open(sorted_full_path, 'w', encoding = 'utf-8') as file_to_write:
    for i in sorted_len:
        file_to_write.write(all_texts[i]['name'] + '\n' + all_texts[i]['length'] + '\n' + all_texts[i]['text'] + '\n')