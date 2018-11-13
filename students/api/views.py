
# generic -> convenient
# generic views from docs

from rest_framework import generics
from students.models import Student
from .serlializers import StudentSerializer


class StudentRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()
