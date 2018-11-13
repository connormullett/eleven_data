
from .views import StudentRudView
from django.urls import path, include
from .views import StudentRudView

urlpatterns = [
    path('/<int:pk>', StudentRudView.as_view(), name='student-rud')
]
