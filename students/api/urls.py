
from .views import StudentRudView
from django.urls import path, include
from .views import StudentRudView, CreateStudent

urlpatterns = [
    path('<int:pk>', StudentRudView.as_view(), name='student-rud'),
    path('', CreateStudent.as_view(), name='student-create')
]
