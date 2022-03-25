import json

print("Поиск:")
print("По названию коктейля [1]")
print("По основе коктейля [2]")
print("По основе вместе с рецептами [3]")
print("Список шотов с рецептами [4]")
print("Выход [0]")

choice = int(input("Ввод:>>> "))

volumes = {'shot': 'стопку', 'short': 'стопку'}


def search_by_name():
    query = input('Введите название коктейля: ')
    query = query.capitalize()
    if query in file.keys():
        print('>>>', query, ':')
        for item in file[query][0]:
            print(item)


def search_by_base():
    ingredient = input('Введите основу: ')
    for name_of_cocktail, list_ingredients in file.items():
        if ingredient.lower() in list_ingredients[0][0] or ingredient.capitalize() in list_ingredients[0][0]:
            print(name_of_cocktail)


def search_by_base_with_recipes():
    ingredient = input('Введите основу: ')
    for name_of_cocktail, list_ingredients in file.items():
        if ingredient.lower() in list_ingredients[0][0] or ingredient.capitalize() in list_ingredients[0][0]:
            print(name_of_cocktail, ':')
            for item in list_ingredients[0]:
                print(item)
            print('-----------------------------')


def shots():
    for name_of_cocktail, list_ingredients in file.items():
        for element in list_ingredients[0]:
            if 'стопку' in element:
                print('-----------------------')
                print(name_of_cocktail, ':')
                for s in list_ingredients[0]:
                    print(s)
                break


with open("cocktails_recipes_dict.json", 'r', encoding='windows-1251') as file:
    file = file.read()
    file = json.loads(file)
    while 1 <= choice <= 4:
        if choice == 1:
            search_by_name()
        elif choice == 2:
            search_by_base()
        elif choice == 3:
            search_by_base_with_recipes()
        elif choice == 4:
            shots()
        else:
            print('error')
        choice = int(input("Ввод:>>> "))