from django.urls import path

from .views import index, by_category
from .views import PeopleCreateView

urlpatterns = [
    path('add/', PeopleCreateView.as_view(), name='add'),
    path('<int:category_id>/', by_category, name='by_category'),
    path('', index, name='index'),
]