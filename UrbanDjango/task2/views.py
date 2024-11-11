from django.shortcuts import render
from django.views.generic import TemplateView


# Создание функционального представления.
def func_function(request):
    return render(request, 'second_task/func_template.html')

# Создание классового представления (стандартный вариант)
# class ClassView(TemplateView):
#     template_name = 'second_task/class_template.html'

