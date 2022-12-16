from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import facultyForm
from .models import Availability, WEEK_DAY_CHOICES, COLLEGE_CHOICES, COURSE_CHOICES


# Ref 1: https://stackoverflow.com/questions/2245895/is-there-a-simple-way-to-get-group-names-of-a-user-in-django
@login_required(login_url='/account/login/')
def profile(request):
    # TODO
    return render(request, 'home/profile.html', {})


@login_required(login_url='/account/login/')
def schedules(request):
    # TODO
    return render(request, 'home/schedules.html', {})


@login_required(login_url='/account/login/')
def department(request):
    # TODO
    return render(request, 'home/department.html', {})


@login_required(login_url='/account/login/')
def faculty(request):
    # TODO
    return render(request, 'home/faculty.html', {})


@login_required(login_url='/account/login/')
def faculty_form(request):

    if request.method == 'POST':
        # TODO
        form = facultyForm(data=request.POST)

        if form.is_valid():
            form.save()

    form = facultyForm()

    # Dito i-dedefine ko na yung mga needed like colleges, departments, weeks.
    # Ginawa ko yun para yun lng need baguhin ng admin if may changes
    # na gagagawin hindi yung pupuntahan pa nila yung html file para mag bago.
    return render(request, "home/faculty-form.html", {
        "form": form,
        "weeks": WEEK_DAY_CHOICES,
        "colleges": COLLEGE_CHOICES,
        "departments": COURSE_CHOICES,
    })
