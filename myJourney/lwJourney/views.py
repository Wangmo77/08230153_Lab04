from django.shortcuts import render
from .models import Student, Learning_Activity

def index(request):
    try:
        # Get your specific student record (adjust the name if needed)
        student = Student.objects.get(name='Leki Wangmo')
        activities = Learning_Activity.objects.filter(student=student)
        context = {
            'student': student,
            'activities': activities
        }
    except Student.DoesNotExist:
        context = {
            'student': None,
            'activities': []
        }
    return render(request, 'index.html', context)


def aboutMe(request):
    try:
        # Get your specific student record (adjust the name if needed)
        student = Student.objects.get(name='Leki Wangmo')
        context = {
            'student': student
        }
    except Student.DoesNotExist:
        context = {
            'student': None
        }
    return render(request, 'aboutMe.html', context)
    