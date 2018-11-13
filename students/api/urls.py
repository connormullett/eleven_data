
from .views import StudentRudView
from django.urls import path, include
from .views import StudentRudView

url_patterns = [
    path('<int:id>', StudentRudView.as_view(), name='student-rud')
]
