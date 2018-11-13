
# generic -> convenient
# generic views from docs

from rest_framework import generics
from students.models import Student
from .serlializers import StudentSerializer


class ListStudent(generics.ListAPIView):
    lookup_field = 'pk'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()


class StudentRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()


class CreateStudent(generics.CreateAPIView):
    lookup_field = 'pk'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()
