from .form import AddCourseForm, DescriptionForm, AddComment
from django.shortcuts import render, redirect
from .models import Course, Description

def index(request):
    form = AddCourseForm()
    desc = DescriptionForm()
    context = {
        'form': form,
        'courses': Course.objects.all(),
        'desc': desc
    }
    return render(request, "coursesApp/index.html", context)

def add(request):
    new_course = Course.objects.create(course_name=request.POST['course_name'])
    Description.objects.create(description = request.POST['description'], courses_description = new_course)
    return redirect('/')

def desc(request, course_id, description_id):
    course = Course.objects.get(id=course_id)
    desc = Description.objects.get(id=description_id)
    form = AddComment()
    context = {
        'course': course,
        'description': desc,
        'comment': form
    }
    return render(request, "coursesApp/description.html", context)

def delete(request, course_id, description_id):
    course = Course.objects.get(id=course_id)
    desc = Description.objects.get(id=description_id)
    course.delete()
    desc.delete()
    return redirect('/')
# Create your views here.
