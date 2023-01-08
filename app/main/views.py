from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FacultyForm, AvailabilityForm
from .models import Availability, WEEK_DAY_CHOICES, COLLEGE_CHOICES, COURSE_CHOICES, Department, Course, Faculty


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

        fform = FacultyForm(data=request.POST)
        aform = AvailabilityForm(data=request.POST)

        if fform.is_valid() and aform.is_valid():
            # Get the id for the availability table
            school_id = fform.cleaned_data['school_id']
            fform.save()

            # Query the id of created faculty data for availabilty
            faculty_id = Faculty.objects.get(school_id=school_id)
            aform.instance.faculty_id_id = faculty_id.id
            aform.save()

    fform = FacultyForm()
    aform = AvailabilityForm()
    # Dito i-dedefine ko na yung mga needed like colleges, departments, weeks.
    # Ginawa ko yun para yun lng need baguhin ng admin if may changes
    # na gagagawin hindi yung pupuntahan pa nila yung html file para mag bago.
    return render(request, "home/faculty-form.html", {
        "availability_form": aform,
        "faculty_form": fform,
        "weeks": WEEK_DAY_CHOICES,
    })


def load_courses(request):
    department_id = request.GET.get('college_id')
    courses = Course.objects.filter(college_id=department_id)
    return render(request, 'home/course_list.html', {'courses': courses})
