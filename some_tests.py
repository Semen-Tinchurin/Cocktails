import json

print("Поиск:")
print("По названию коктейля [1]")
print("По основе коктейля [2]")
print("По основе вместе с рецептами [3]")
print("Выход [0]")

choice = int(input("Ввод:>>> "))

with open("cocktails_recipes_dict.json", 'r', encoding='windows-1251') as file:
    file = file.read()
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
                for item in list_ingredients[0]:
                    if num == 0:
                        if ingredient.lower() in item:
                            print(name_of_cocktail)
                            num += 1
                    else:
                        break

        elif choice == 3:
            ingredient = input('Введите основу: ')
            for name_of_cocktail, list_ingredients in file.items():
                num = 0
                for item in list_ingredients[0]:
                    if num == 0:
                        if ingredient.lower() in item:
                            print(name_of_cocktail, ':')
                            for item2 in list_ingredients[0]:
                                print(item2)
                            print("--------")
                            num += 1
                    else:
                        break

        else:
            print('error')

        choice = int(input("Ввод:>>> "))