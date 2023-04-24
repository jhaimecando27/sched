from django.contrib import admin
# from .models import facultyMemberForm

# Register your models here.
# admin.site.register(facultyMemberForm)

from .models import (Subject, Schedule, Professor,
                     Chairperson, Course, Department, Room)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('course', 'code', 'name', 'units')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('subject', 'block_number',
                    'week_day', 'start_time', 'end_time')


class ChairpersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'employment_status')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('bldg_code', 'bldg_name', 'room_num')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Chairperson, ChairpersonAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Room, RoomAdmin)
