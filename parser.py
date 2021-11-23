import requests
import json
import csv
import time
from bs4 import BeautifulSoup
# url = 'https://ru.inshaker.com/cocktails?random_page=59'

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63 (Edition Yx 05)"
}
# req = requests.get(url, headers=headers)
#
# src = req.text
# print(src)
#
# with open("all_cocktails.html", "r", encoding="utf-8-sig") as file:
#     src = file.read()
#
#
# soup = BeautifulSoup(src, 'lxml')
# all_cocktails_hrefs = soup.find_all(class_="cocktail-item-preview")
#
# all_cocktails_links_dict = {}
# for item in all_cocktails_hrefs:
#     cocktail_name = item.text
#     cocktail_href = "https://ru.inshaker.com" + item.get('href')
#     print(f"{cocktail_name}: {cocktail_href}")
#     all_cocktails_links_dict[cocktail_name] = cocktail_href
#
# with open("all_cocktails_links_dict.json", "w") as file:
#     json.dump(all_cocktails_links_dict, file, indent=4, ensure_ascii=False)


start_time = time.time()

with open("all_cocktails_links_dict.json") as file:
    all_cocktails = json.load(file)

all_cocktails_recipe_dict = {}
for cocktail_name, cocktail_href in all_cocktails.items():
    req = requests.get(url=cocktail_href, headers=headers)

    src = req.text
    soup = BeautifulSoup(src, 'lxml')

# Собираем ингридиенты:

    def search_ingridients_and_recipe():
        list_of_ingridients_and_pecipes = []
        ingridients = soup.find('table')
        rec = soup.find(class_='steps')
        for ing in ingridients:
            list_of_ingridients_and_pecipes.append(ing.text)
        del list_of_ingridients_and_pecipes[0]

        for r in rec:
            list_of_ingridients_and_pecipes.append(r.text)
        all_cocktails_recipe_dict[cocktail_name] = [list_of_ingridients_and_pecipes]

        # записываем в .json формат
        with open("cocktails_recipes_dict.json", "w") as file:
            json.dump(all_cocktails_recipe_dict, file, indent=4, ensure_ascii=False)

    search_ingridients_and_recipe()

end_time = time.time()

print(all_cocktails_recipe_dict)
print(end_time-start_time)


# заняло 1265.828206539154 секунд
# заняло 1526.577917098999 секунд

