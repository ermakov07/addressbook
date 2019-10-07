from django.shortcuts import render

from .models import ListPeople


def index(request):
    ListPeople_s = ListPeople.objects.all()

    return render(request, 'pogoda/index.html', {'ListPeople_s': ListPeople_s})