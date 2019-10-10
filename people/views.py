from django.shortcuts import render

from .models import ListPeople
from .models import Category


def index(request):
    lp = ListPeople.objects.all()
    categories = Category.objects.all()
    context = {'lp': lp, 'categories': categories}
    return render(request, 'people/index.html', context)

def by_category(request, category_id):
    lp = ListPeople.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'lp': lp, 'categories': categories, 'current_category': current_category}
    return render(request, 'people/by_category.html', context)

