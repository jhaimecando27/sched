from django.db import models
from django.contrib.auth.models import User

EMPLOYMENT_TYPE_CHOICES = (
    ('PT', 'Part Time'),
    ('FT', 'Full Time'),
)

WEEK_DAY_CHOICES = (
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday'),
)

COLLEGE_CHOICES = (
    ('CET', 'College of Engineering and Technology'),
)

COURSE_CHOICES = (
    ('BSCS', 'Bachelor of Science in Computer Science'),

    ('BSCHE', 'Bachelor of Science in Chemical Engineering'),

    ('BSCE', 'Bachelor of Science in Civil Engineering'),
)


class extendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_chairperson = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)


class Department(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.code


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=80, unique=True)
    college_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    chairperson_id = models.ForeignKey(User, on_delete=models.CASCADE)
    num_blocks = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Subject(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    units = models.IntegerField(default=False)


class Room(models.Model):
    bldg_initials = models.CharField(max_length=100)
    bldg_name = models.CharField(max_length=100)
    room_num = models.IntegerField()


class Schedule(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    block_number = models.IntegerField()
    week_day = models.CharField(choices=WEEK_DAY_CHOICES, max_length=3)
    day_time = models.TimeField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)


class Faculty(models.Model):
    school_id = models.IntegerField(blank=True, null=True, unique=True)
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    employment_status = models.CharField(
        choices=EMPLOYMENT_TYPE_CHOICES, max_length=10)
    schedule_id = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, blank=True, null=True)
    total_units = models.IntegerField(blank=True, null=True)
    college_id = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Availability(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    week_day = models.CharField(choices=WEEK_DAY_CHOICES, max_length=3)
    start_time = models.TimeField()
    end_time = models.TimeField()
