from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from people.models import ListPeople
from people.models import Category
from people.forms import PeopleForm
from people.forms import CategoryForm

from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import RubricSerializer
from api.serializers import PeopleSerializer


@api_view(['GET'])
def api_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = RubricSerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_category(request, category_id):
    if request.method == 'GET':
        categories = Category.objects.all()
        current_category = Category.objects.get(pk=category_id)
        lp = current_category.listpeople_set.all()
        serializer = PeopleSerializer(lp, many=True)
        return Response(serializer.data)