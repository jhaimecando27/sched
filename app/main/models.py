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


class Department(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.code


class Course(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=80, unique=True)
    num_blocks = models.IntegerField(default=0)

    def __str__(self):
        return self.code


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=64)
    units = models.IntegerField(default=0)

    def __str__(self):
        return self.code


class Room(models.Model):
    bldg_code = models.CharField(max_length=100)
    bldg_name = models.CharField(max_length=100)
    room_num = models.IntegerField()

    def __str__(self):
        return self.bldg_code


class Chairperson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Professor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    employment_status = models.CharField(
        choices=EMPLOYMENT_TYPE_CHOICES, max_length=40)
    expertise = models.CharField(default="None", max_length=64)
    total_units = models.IntegerField(default=False)


class Preference(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    week_day = models.CharField(
        choices=WEEK_DAY_CHOICES, max_length=40)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Schedule(models.Model):
    chairperson = models.ForeignKey(Chairperson, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    block_number = models.IntegerField()
    week_day = models.CharField(choices=WEEK_DAY_CHOICES, max_length=3)
    start_time = models.TimeField()
    end_time = models.TimeField()
