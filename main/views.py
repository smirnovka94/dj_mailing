from django.shortcuts import render

from main.models import StatusMailing


def home(request):
    context = {
        'object_list': StatusMailing.objects.all(),
        'title': 'Skystore',
        'title_comments': 'Skystore - это отличный вариант выбора товара на любой вкус!'
    }
    return render(request, 'main/home.html', context)