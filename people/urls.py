from django.urls import path

from .views import index, by_category
from .views import PeopleCreateView
from .views import CategoryCreateView


urlpatterns = [
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('add/', PeopleCreateView.as_view(), name='add'),
    path('<int:category_id>/', by_category, name='by_category'),
    path('', index, name='index'),
]
