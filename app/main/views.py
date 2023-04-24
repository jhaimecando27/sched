from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.contrib.auth.decorators import login_required
from .forms import (SubjectForm, RoomForm, BlockForm)
from .models import (EMPLOYMENT_TYPE_CHOICES, WEEK_DAY_CHOICES, Preference,
                     Department, Course, Professor, Chairperson, Subject, Room)

# Ref 1: https://stackoverflow.com/questions/2245895/is-there-a-simple-way-to-get-group-names-of-a-user-in-django


@login_required(login_url='/account/login/')
def profile(request):

    # course = None
    # current_user = request.user
    # course_id = None
    # course_title = None
    # dept_id = None

    # if request.session['is_chairperson'] == True:
    #     course = Course.objects.filter(chairperson_id=current_user.id).first()
    #     course_id = course.id
    #     course_title = course.title
    #     dept_id = course.college_id
    # elif request.session['is_professor'] == True:
    #     faculty = Faculty.objects.filter(user=current_user.id).first()
    #     course_id = faculty.course_id
    #     course = Course.objects.filter(id=faculty.course_id.id).first()
    #     course_title = course.title
    #     dept_id = course.college_id

    # list_chair = Course.objects.all().select_related(
    #     'chairperson_id').select_related('college_id').filter(college_id=dept_id.id)

    # dept_title = dept_id.title

    # faculty_pt = Faculty.objects.all().filter(
    #     course_id=course_id, employment_status=EMPLOYMENT_TYPE_CHOICES[0][0]).count()
    # faculty_ft = Faculty.objects.all().filter(
    #     course_id=course_id, employment_status=EMPLOYMENT_TYPE_CHOICES[1][0]).count()
    # faculty_all = Faculty.objects.all().filter(course_id=course_id).count()

    # ave_pt = (faculty_pt / faculty_all) * 100
    # ave_ft = (faculty_ft / faculty_all) * 100

    # context = {
    #     'current_user': current_user,
    #     'ave_pt': ave_pt,
    #     'ave_ft': ave_ft,
    #     'faculty_ft': faculty_ft,
    #     'faculty_pt': faculty_pt,
    #     'course_title': course_title,
    #     'dept_title': dept_title,
    #     'list_chair': list_chair,
    # }

    return render(request, 'home/profile.html', {})


@login_required(login_url='/account/login/')
def create_schedule(request):
    # TODO
    return render(request, 'home/create_schedule.html', {})


@login_required(login_url='/account/login/')
def schedule(request):
    # TODO
    return render(request, 'home/schedule.html', {})


@login_required(login_url='/account/login/')
def subject(request):
    current_user = request.user
    course = Course.objects.filter(chairperson=current_user.id).first()
    college = Department.objects.get(id=course.dept.id)
    list_subjs = Subject.objects.filter(course=course.id)

    # POST
    if request.method == 'POST':
        # Initialze form
        form = SubjectForm(data=request.POST)

        # Get & Check Form
        if form.is_valid():
            subj = form.save(commit=False)
            subj.course_id = course.id
            subj.save()

    form = SubjectForm()

    context = {
        'college': college,
        'list_subjs': list_subjs,
        'form': form,
    }

    return render(request, 'home/department/subject.html', context)


@login_required(login_url='/account/login/')
def room(request):
    current_user = request.user
    course = Course.objects.filter(chairperson=current_user.id).first()
    college = Department.objects.get(id=course.dept.id)
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

    return render(request, 'home/department/room.html', context)


@login_required(login_url='/account/login/')
def block(request):
    current_user = request.user
    course = Course.objects.filter(chairperson=current_user.id).first()
    college = Department.objects.get(id=course.dept.id)

    # POST
    if request.method == 'POST':
        # Initialze form
        form = BlockForm(data=request.POST)

        # Get & Check Form
        if form.is_valid():
            num_blocks = form.cleaned_data['num_blocks']
            course.num_blocks = num_blocks
            course.save()

    form = BlockForm()

    context = {
        'college': college,
        'course': course,
        'form': form,
    }

    return render(request, 'home/department/block.html', context)


@login_required(login_url='/account/login/')
def faculty(request):
    current_user = request.user
    course = Course.objects.filter(chairperson=current_user.id).first()
    college = Department.objects.get(id=course.dept.id)
    list_prof = Professor.objects.filter(
        id=course.id).select_related('user')

    context = {
        'list_prof': list_prof,
        'college': college
    }

    return render(request, 'home/department/faculty.html', context)


def faculty_form(request):

    if request.method == 'POST':

        fform = FacultyForm(data=request.POST)
        aform = AvailabilityForm(data=request.POST)

        if fform.is_valid() and aform.is_valid():
            # # Get the id for the availability table
            # school_id = fform.cleaned_data['school_id']
            # fform.save()
            pass

            # # Query the id of created faculty data for availabilty
            # faculty_id = User.objects.get(school_id=school_id)
            # aform.instance.faculty_id_id = faculty_id.id
            # aform.save()

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
    department_id = request.GET.get('college')
    courses = Course.objects.filter(college_id=department_id)
    return render(request, 'home/course_list.html', {'courses': courses})


@ login_required(login_url='/account/login/')
def del_subj(request, subj_id):
    subject = get_object_or_404(Subject, id=subj_id)

    # TODO: Add try method
    subject.delete()

    return HttpResponseRedirect(reverse('main:subject'))


@ login_required(login_url='/account/login/')
def del_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    # TODO: Add try method
    room.delete()

    return HttpResponseRedirect(reverse('main:room'))
