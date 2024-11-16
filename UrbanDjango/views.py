from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.

def sign_up_by_html(request):
    users = ['Max', 'Alex', 'Olga']
    info = {}
    if request.method == 'POST':
        # получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18 and username not in users:
            users.append(username)
            return HttpResponse(f"Приветствуем, {username}!")  # Ответ пользователю
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse(info['error'])  # Ответ пользователю
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse(info['error'])  # Ответ пользователю
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse(info['error'])  # Ответ пользователю

    # Если это GET-запрос, то отправляем пользователю страницу с формой
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    users = ['Max', 'Alex', 'Olga']
    info = {}
    form = UserRegister(request.POST)
    if form.is_valid():
        # проверка формы на валидацию (доп.параметр для django-формы
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        age = form.cleaned_data['age']
        if password == repeat_password and int(age) >= 18 and username not in users:
            users.append(username)
            return HttpResponse(f"Приветствуем, {username}!")  # Ответ пользователю
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse(info['error'])  # Ответ пользователю
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse(info['error'])  # Ответ пользователю
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse(info['error'])  # Ответ пользователю
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context={'form': form})
