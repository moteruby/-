#Задание5
products = {
    "торт":["шоколадный", 100, 500],
    "пирожное":["клубничное", 50, 100],
    "маффин":["яблочный", 70, 150],
    "пирог":["со сливками", 70, 300],
    "конфеты":["леденцы", 20, 40],
    "шоколад":["с орехами", 20, 20]
}

def show_description(product):
    print("Описание: " + products[product][0])
def show_price(product):
    print("Цена: " + str(products[product][1]))
def show_quantity(product):
    print("Количество: " + str(products[product][2]))
def show_all(product):
    show_description(product)
    show_price(product)
    show_quantity(product)
def buy_product(product, quantity):
    if product in products:
        if products[product][2] >= quantity:
            total_price = products[product][1] * quantity*0.01
            products[product][2] -= quantity
            print("Вы купили " + str(quantity) + " за " + str(total_price))
        else:
            print("Не хватает товара на складе")
    else:
        print("Такого продукта нет в списке")
while True:
    print("Меню:\n1. Просмотр описания;\n2. Просмотр цены;\n3. Просмотр количества\n4. Вся информация\n5. Купить;\n6. Выйти из программы.")
    choice = input("Выберите действие: ")
    match choice.split():
        case ["1"]:
            product = input("Введите название продукта: ")
            if product in products:
                show_description(product)
            else:
                print("Такого продукта нет в списке")
        case ["2"]:
            product = input("Введите название продукта: ")
            if product in products:
                show_price(product)
            else:
                print("Такого продукта нет в списке")
        case ["3"]:
            product = input("Введите название продукта: ")
            if product in products:
                show_quantity(product)
            else:
                print("Такого продукта нет в списке")
        case ["4"]:
            product = input("Введите название продукта: ")
            if product in products:
                show_all(product)
            else:
                print("Такого продукта нет в списке")
        case ["5"]:
            product = input("Введите название продукта: ")
            if product in products:
                quantity = int(input("Введите количество: "))
                buy_product(product, quantity)
            else:
                print("Такого продукта нет в списке")
        case ["6"]:
            break