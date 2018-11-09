
from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.landing, name='landing'),
    path('index', views.student_list, name='index'),
    path('create', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]
