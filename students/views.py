from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})


def create(request):
    pass


def update(request):
    pass


def delete(request):
    pass


# @login_required
def index(request):
    return render(request, 'students/index.html')


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

        context = {
            'form': form
        }

        return render(request, 'registration/register.html', context)


def landing(request):
    return render(request, 'students/landing.html')
