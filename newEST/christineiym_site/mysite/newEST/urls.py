from django.urls import path, include

from .views import index

app_name = 'newEST'
urlpatterns = [
    path('', index, name = 'home'),
]