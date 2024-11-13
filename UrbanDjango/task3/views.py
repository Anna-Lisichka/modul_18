from django.shortcuts import render

# Главная страница создана в упрощенном варианте

# Создание функции, привязанной к шаблону Магазина.
def games(request):
    game1 = 'Mahjong'
    game2 = 'Stalker 2'
    game3 = 'set of games Metro'
    text = 'Купить'
    context = {
        'game1': game1,
        'game2': game2,
        'game3': game3,
        'text': text
    }
    return render(request, 'third_task/games.html', context)


# Создание функции, привязанной к шаблону Корзина.
def cart(request):
    text1 = 'Выбрать способ оплаты'
    text2 = 'Выбрать способ получения '
    context = {
        'text1': text1,
        'text2': text2
    }
    return render(request, 'third_task/cart.html', context)
