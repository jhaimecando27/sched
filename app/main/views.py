from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import facultyForm
from .models import Availability, WEEK_DAY_CHOICES, COLLEGE_CHOICES, COURSE_CHOICES


# Ref 1: https://stackoverflow.com/questions/2245895/is-there-a-simple-way-to-get-group-names-of-a-user-in-django
@login_required(login_url='/account/login/')
def profile(request):
    return render(request, 'home/profile.html', {})


@login_required(login_url='/account/login/')
def schedules(request):
    return render(request, 'home/schedules.html', {})


@login_required(login_url='/account/login/')
def department(request):
    return render(request, 'home/department.html', {})


@login_required(login_url='/account/login/')
def faculty(request):
    return render(request, 'home/faculty.html', {})


@login_required(login_url='/account/login/')
def faculty_form(request):

    if request.method == 'POST':
        form = facultyForm(data=request.POST)

        if form.is_valid():
            form.save()

    form = facultyForm()
    return render(request, "home/faculty-form.html", {
        "form": form,
        "weeks": WEEK_DAY_CHOICES,
        "colleges": COLLEGE_CHOICES,
        "departments": COURSE_CHOICES,
    })
