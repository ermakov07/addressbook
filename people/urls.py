from django.urls import path

from .views import index, by_category, current_people
from .views import PeopleCreateView
from .views import CategoryCreateView


urlpatterns = [
    path('people/<int:listpeople_id>/', current_people, name='people'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('add/', PeopleCreateView.as_view(), name='add'),
    path('<int:category_id>/', by_category, name='by_category'),
    path('', index, name='index'),
]
