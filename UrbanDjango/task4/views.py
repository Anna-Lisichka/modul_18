from django.shortcuts import render


# Создание функции, привязанной к шаблону Главной страницы.
def home_page(request):
    return render(request, 'fourth_task/platform.html')


# Создание функции, привязанной к шаблону Магазина.
def games(request):
    games_list = ['Mahjong', 'Stalker 2', 'set of games Metro']
    text = 'Купить'
    context = {
        'games_list': games_list,
        'text': text,
    }

    return render(request, 'fourth_task/games.html', context)


# Создание функции, привязанной к шаблону Корзина.
def cart(request):
    text1 = 'Выбрать способ оплаты'
    text2 = 'Выбрать способ получения '
    context = {
        'text1': text1,
        'text2': text2
    }
    return render(request, 'fourth_task/cart.html', context)

# Создание функции, привязанной к шаблону Главной страницы.
def menu(request):
    return render(request, 'fourth_task/menu.html')
