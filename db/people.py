from random import randint

def get_employees():
    res = ["Двое из ларца", "кот Бегемот", "Кентервильское привидение", "Колобок"]
    print(res[randint(0, 3)])