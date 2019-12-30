from django.urls import path

from people.views import api_categories
from people.views import api_category


urlpatterns = [
    path('category/<int:category_id>/', api_category),
    path('categories/', api_categories),
]
