
from .views import StudentRudView
from django.urls import path, include
from .views import StudentRudView, CreateStudent, ListStudent

urlpatterns = [
    path('<int:pk>', StudentRudView.as_view(), name='student-rud'),
    path('create', CreateStudent.as_view(), name='student-create'),
    path('list', ListStudent.as_view(), name='student-list')
]
