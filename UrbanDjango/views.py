from django.shortcuts import render


# Создание функции, привязанной к шаблону Магазина.
def games(request):
    return render(request, 'third_task/games.html')


# Создание функции, привязанной к шаблону Корзина.
def cart(request):
    text1 = 'Выбрать способ оплаты'
    text2 = 'Выбрать способ получения '
    context = {
        'text1': text1,
        'text2': text2
    }
    return render(request, 'third_task/cart.html', context)