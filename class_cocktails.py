import json

LONG_DRINK_GLASSES = ["Харрикейн", "Хайбол", "Слинг", "Бокал для вина", "Коллинз", "Кубок",
                      "Тики-бокал", "Коктейльная креманка", "Пинта", "Калабас"]
SHORT_DRINK_GLASSES = ["Коктейльный бокал", "Рокс", "Шампанское блюдце", "Бокал для ирландского кофе",
                       "Флюте", "Бокал сауэр", "Чашка", "Медная кружка", "Коньячный бокал", "Бокал маргарита",
                       "Коническая колба", "Пластиковый стакан", "Банка с крышкой"]
SHOT_GLASSES = ['Стопка', "Пробирка"]


class Cocktails():

    def __init__(self, file_name):
        self.file_name = file_name
        self.dict_of_cocktail = {}
        self.ingredients = []
        self.recipe = []
        self.things = []
        self.name = None

    def reading(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            file = file.read()
            file = json.loads(file)
            self.dict_of_cocktail = file

    def outparse(self):
        for key, values in self.dict_of_cocktail.items():
            self.ingredients = values[0]
            self.things = values[1]
            self.recipe = values[2]
            self.name = key

            print(self.name)
            print(self.ingredients)
            print(self.things)
            print(self.recipe)


file_with_recipes = Cocktails(file_name='test_output_1.json')
file_with_recipes.reading()
file_with_recipes.outparse()
