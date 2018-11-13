
from django.contrib import admin
from django.urls import path, include
from students import views

urlpatterns = [
    path('', views.landing),
    path('api/students/', include('students.api.urls'), name='api-students'),
    path('students/', include('students.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
