from django.shortcuts import render, redirect
from .models import Students

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')

        # Save the student
        Students.objects.create(name=name, email=email, course=course)
        return redirect('home')

    all_students = Students.objects.all()
    return render(request, 'home.html', {'Students': all_students})
