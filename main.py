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

def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for item in dishes: 
        if item not in cook_book.keys():
            error = 'Ошибка: введённого Вами блюда нет в кулинарной книге'
            return error
        for key, values in cook_book.items():
            if item in key:
                for value in values:
                    ingredients_info = {}
                    shop_dict_ingredient = value['ingredient_name']
                    shop_dict[shop_dict_ingredient] = ingredients_info
                    ingredients_info['measure'] = value['measure']
                    if 'quantity' not in ingredients_info.keys():
                        ingredients_info['quantity'] = int(value['quantity']) * person_count
                    else:
                        new_quantity = ingredients_info['quantity'] + (int(value['quantity']) * person_count)
                        ingredients_info['quantity'] = new_quantity
    return shop_dict

#pprint(cook_book, sort_dicts=False, width=100)
#pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Запеченный картофель'], 3), sort_dicts=False)

# упорно не получается обыграть сценарий с повторением игредиентов, гуглила и спрашивала в дискорде и телеграме 
# в соответствующих чатах - тоже не смогли помочь. Если оставляю в третьем цикле, то не прибавляется значение к повторяющемуся
# ингредиенту, если ставлю в циклы раньше, то количества неверные уже у всех ингредиентов. 
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2), sort_dicts=False) 