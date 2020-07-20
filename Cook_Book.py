import pprint
from collections import Counter

cook_book = {}


def get_cook_book():
    with open('Book.txt', encoding='utf-8') as f:
        while True:
            menu = f.readline().strip()
            ingredients_list = []
            if not menu:
                break
            amount = int(f.readline().strip())
            while amount > 0:
                ingredients = [f.readline().strip().split(' | ')]
                amount -= 1
                for ingredient in ingredients:
                    ingredients_list.append({'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
            f.readline()
            cook_book.update({menu: ingredients_list})
    print(cook_book)
    print()
    pprint.pprint(cook_book)
    print()
get_cook_book()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes_dict = {}

    for value in Counter(dishes).values():
        pass

    for dish in dishes:
        for element in cook_book[dish]:
            shop_list_by_dishes_dict[element['ingredient_name']] = {'quantity': int(element['quantity']) * person_count * value, 'measure': element['measure']}
    print(shop_list_by_dishes_dict)
    print()
    pprint.pprint(shop_list_by_dishes_dict)


get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)