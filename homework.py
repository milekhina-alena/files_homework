# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

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
        # cook_book.append(cook_book_page)
        

print(cook_book)
print(len(cook_book))


