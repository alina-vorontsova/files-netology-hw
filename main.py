from pprint import pprint


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

#pprint(cook_book, sort_dicts=False, width=100)
#pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Запеченный картофель'], 3), sort_dicts=False)
#pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2), sort_dicts=False) 