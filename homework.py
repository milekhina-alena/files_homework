cook_book = {}

with open('cook_book.txt', 'r') as recipes:
    for line in recipes:
        meal_name = line.strip()
        cook_book[meal_name] = []
        ingredients_count = recipes.readline()
        for i in range(int(ingredients_count)):
            ing = recipes.readline()
            ingredient_name, quantity, measure = ing.split(' | ')
            ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
            cook_book[meal_name].append(ingredient)
        recipes.readline()
        

# print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):

    shop_list = {}
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            index = 0
            while index < len(ingredients):
                if ingredients[index]['ingredient_name'] in shop_list.keys():
                    for v in shop_list.values():
                        v['quantity'] += int(ingredients[index]['quantity']) * person_count
                else:
                    measure = ingredients[index]['measure']
                    quantity = int(ingredients[index]['quantity']) * person_count
                    shop_list[ingredients[index]['ingredient_name']] = {'measure': measure, 'quantity': quantity}
                index += 1
    res = shop_list
    return res


# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
# print(get_shop_list_by_dishes(['Утка по-пекински'], 2))











