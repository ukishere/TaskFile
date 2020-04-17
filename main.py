def cook_book_creation(receipts_file):
    cook_book = {}
    stage = 0
    count = 0
    name = ''
    ingredients = []

    for line in receipts_file:
        line = line.rstrip('\n')

        if stage == 0:
            name = line
            stage = 1
        elif stage == 1:
            count = int(line)
            stage = 2
        elif stage == 2:
            if count != 0:
                ingredient = line.split(' | ')
                ingredients.append({'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
                count -= 1
            else:
                cook_book[name] = ingredients
                ingredients = []
                stage = 0

    cook_book[name] = ingredients
    return cook_book

def shop_list(list_of_dishes, persons):
    persons = int(persons)
    dishes = []
    if type(list_of_dishes) == str:
        dishes = [list_of_dishes]
    elif type(list_of_dishes) == list:
        dishes = list_of_dishes
    else:
        print('Неверно передан список блюд')

    count = len(dishes)

    receipts_file = open('receipts.txt', 'r')
    cook_book = cook_book_creation(receipts_file)
    receipts_file.close()

    final_list = {}

    while count != 0:
        if cook_book.get(dishes[count-1]) == None:
            print(f'В кулинарной книге нет {dishes[count-1]}')
        else:
            for dish in cook_book[dishes[count-1]]:
                ingredient = dish['ingredient_name']
                quantity = int(dish['quantity']) * persons
                measure = dish['measure']

                if final_list.get(ingredient) != None:
                    quantity = quantity + final_list[ingredient]['quantity']

                final_list[ingredient] = {'measure': measure, 'quantity': quantity}

        count -= 1

    return final_list

print(shop_list(['Омлет', 'Утка по-пекински', 'Запеченный картофель', 'Фахитос'], 5))

