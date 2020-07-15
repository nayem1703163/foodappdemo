from django.contrib import admin
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.restaurant_list_which_comes_from_database.as_view()),
]
