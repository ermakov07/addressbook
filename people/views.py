from django.shortcuts import render

from .models import ListPeople


def index(request):
    lp = ListPeople.objects.all()
    return render(request, 'people/index.html', {'lp': lp})