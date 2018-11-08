from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})


def create(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    if request.method == "GET":
        return render(request, 'students/student_form.html', {'form': form})


def update(request):
    pass


def delete(request):
    pass


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('')
    else:
        form = UserCreationForm()

        context = {
            'form': form
        }

        return render(request, 'registration/register.html', context)


def landing(request):
    return render(request, 'students/landing.html')
