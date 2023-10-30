from django.shortcuts import redirect, render, HttpResponse
from .models import *


# Create your views here.
def home(request):
    queryset = Student.objects.all()
    if request.GET.get("searchroll"):
        queryset = Student.objects.filter(
            rollno__icontains=request.GET.get("searchroll")
        )
    context = {
        "students": queryset,
    }
    return render(request, "index.html", context)


def add_student(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        rollno = data.get("rollno")
        rollno = rollno.upper()
        email = data.get("email")
        mobile = data.get("mobile")
        gender = data.get("gender")
        batch = data.get("batch")
        profile_image = request.FILES.get("profile_image")
        Student.objects.create(
            name=name,
            rollno=rollno,
            email=email,
            mobile=mobile,
            gender=gender,
            batch=batch,
            profile_image=profile_image,
        )

        return redirect("/")
    queryset = Student.objects.all()
    context = {
        "students": queryset,
    }
    return render(request, "add_student.html", context)


def delete_student(request, rollno):
    student = Student.objects.get(rollno=rollno)
    student.delete()
    return redirect("/studentslist/")


def update_student(request, rollno):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        rollno = data.get("rollno")
        email = data.get("email")
        mobile = data.get("mobile")
        gender = data.get("gender")
        batch = data.get("batch")
        profile_image = request.FILES.get("profile_image")
        Student.objects.filter(rollno=rollno).update(
            name=name,
            rollno=rollno,
            email=email,
            mobile=mobile,
            gender=gender,
            batch=batch,
            profile_image=profile_image,
        )
        return redirect("/studentslist/")

    student = Student.objects.get(rollno=rollno)
    context = {"student": student}
    return render(request, "update_student.html", context)
