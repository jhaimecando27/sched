from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .forms import FacultyForm, AvailabilityForm, SubjectForm, RoomForm, CourseForm
from .models import Availability, WEEK_DAY_CHOICES, COLLEGE_CHOICES, COURSE_CHOICES, Department, Course, Faculty, Subject, Room


# Ref 1: https://stackoverflow.com/questions/2245895/is-there-a-simple-way-to-get-group-names-of-a-user-in-django
@login_required(login_url='/account/login/')
def profile(request):
    current_user = request.user

    return render(request, 'home/profile.html', {'current_user': current_user})


@login_required(login_url='/account/login/')
def schedules(request):
    # TODO
    return render(request, 'home/schedules.html', {})


@login_required(login_url='/account/login/')
def subject(request):
    current_user = request.user
    course = Course.objects.filter(chairperson_id=current_user.id).first()
    college = Department.objects.get(id=course.college_id.id)
    list_subjs = Subject.objects.filter(course_id_id=course.id)

    # POST
    if request.method == 'POST':
        # Initialze form
        form = SubjectForm(data=request.POST)

        # Get & Check Form
        if form.is_valid():
            subj = form.save(commit=False)
            subj.course_id_id = course.id
            subj.save()

    form = SubjectForm()

    context = {
        'college': college,
        'list_subjs': list_subjs,
        'form': form,
    }

    return render(request, 'home/subject.html', context)


@login_required(login_url='/account/login/')
def room(request):
    current_user = request.user
    course = Course.objects.filter(chairperson_id=current_user.id).first()
    college = Department.objects.get(id=course.college_id.id)
    list_rooms = Room.objects.all()

    # POST
    if request.method == 'POST':
        # Initialze form
        form = RoomForm(data=request.POST)

        # Get & Check Form
        if form.is_valid():
            form.save()

    form = RoomForm()

    context = {
        'college': college,
        'list_rooms': list_rooms,
        'form': form,
    }

    return render(request, 'home/room.html', context)


@login_required(login_url='/account/login/')
def block(request):
    current_user = request.user
    course = Course.objects.filter(chairperson_id=current_user.id).first()
    college = Department.objects.get(id=course.college_id.id)

    # POST
    if request.method == 'POST':
        # Initialze form
        form = CourseForm(data=request.POST)

        # Get & Check Form
        if form.is_valid():
            form.save()

    form = RoomForm()

    context = {
        'college': college,
        'course': course,
        'form': form,
    }

    return render(request, 'home/block.html', context)


@login_required(login_url='/account/login/')
def faculty(request):
    current_user = request.user
    course = Course.objects.filter(chairperson_id=current_user.id).first()
    college = Department.objects.get(id=course.college_id.id)
    list_faculty = Faculty.objects.filter(course_id=course.id)

    context = {
        'list_faculty': list_faculty,
        'college': college
    }

    return render(request, 'home/faculty.html', context)


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


@login_required(login_url='/account/login/')
def del_subj(request, subj_id):
    subject = get_object_or_404(Subject, id=subj_id)

    # TODO: Add try method
    subject.delete()

    return HttpResponseRedirect(reverse('main:subject'))


@login_required(login_url='/account/login/')
def del_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    # TODO: Add try method
    room.delete()

    return HttpResponseRedirect(reverse('main:room'))
