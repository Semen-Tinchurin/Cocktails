#!/usr/bin/python3
import json


def __main__():
    print("Поиск:")
    print("По названию коктейля [1]")
    print("По основе вместе с рецептами [2] ")
    print("По основе коктейля [3] ")
    print("Выход [0]")

    # python3 -m cocktails -n "name" | -b "base" | -B "cocktail base"
    # ((?:[А-Яа-я]+\s+)+)(\d+)([А-Яа-я]+)

    choice = int(input("Ввод:>>> "))

    file = None

    with open("cocktails_recipes_dict.json", 'r', encoding='windows-1251') as json_file:
        file = json_file.read()
        file = json.loads(file)

    while 1 <= choice <= 3:
        if choice == 1:
            query = input('Введите название коктейля: ')
            query = query.capitalize()
            if query in file.keys():
                print('>>>', query, ':')
                for item in file[query][0]:
                    print(item)

        elif choice == 2:
            ingredient = input('Введите основу: ')
            for name_of_cocktail, list_ingredients in file.items():
                num = 0
                if num == 0:
                    if ingredient.lower() in list_ingredients[0][0]:
                        print(name_of_cocktail, ':')
                        for item2 in list_ingredients[0]:
                            print(item2)
                        print("--------------------------------------------------")
                        num += 1
                else:
                    break

        elif choice == 3:
            ingredient = input('Введите основу: ')
            for name_of_cocktail, list_ingredients in file.items():
                num = 0
                if num == 0:
                    if ingredient.lower() in list_ingredients[0][0]:
                        print(name_of_cocktail)
                        num += 1
                else:
                    break

        else:
            print('error')

        choice = int(input("Ввод:>>> "))


__main__()
