from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import ListPeople
from .models import Category
from .forms import PeopleForm
from .forms import CategoryForm


class PeopleCreateView(CreateView):
    template_name = 'people/create.html'
    form_class = PeopleForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryCreateView(CreateView):
    template_name = 'people/create_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('index')


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

