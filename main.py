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
            ingredients_dict['quantity'] = quantity
            ingredients_dict['measure'] = measure.strip()
            ingredients_list.append(ingredients_dict)
        cook_book[dish_name] = ingredients_list
        file_object.readline()

#pprint(cook_book, sort_dicts=False, width=100)

def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for item in dishes: 
        if item not in cook_book.keys():
            error = 'Ошибка: введённого Вами блюда нет в кулинарной книге'
            return error 
        for key, values in cook_book.items():
            if item in key:
                ingredients_info = {}
                for value in values:
                    ingredients_info = {}
                    shop_dict_ingredient = value['ingredient_name'] 
                    if shop_dict_ingredient not in shop_dict.keys():
                        shop_dict[shop_dict_ingredient] = {}
                        ingredients_info['measure'] = value['measure']
                        ingredients_info['quantity'] = int(value['quantity']) * person_count
                        shop_dict[shop_dict_ingredient] = ingredients_info
                    else: 
                        new_quantity = ingredients_info['quantity'] + (int(value['quantity']) * person_count)
                        ingredients_info['quantity'] = new_quantity
    pprint(shop_dict, sort_dicts=False)



print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))

