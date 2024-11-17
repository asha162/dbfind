from django.urls import path
from . import views

urlpatterns = [
    path('find_data/', views.find_data, name='find_data'),
]
