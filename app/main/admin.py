from django.contrib import admin
# from .models import facultyMemberForm

# Register your models here.
# admin.site.register(facultyMemberForm)

from .models import (
    Subject, Schedule, Faculty, Availability, Course, Department, Room, extendUser)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'code', 'title', 'units')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('subject_id', 'block_number', 'week_day', 'day_time')


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('user', 'employment_status',
                    'schedule_id', 'total_units', 'course_id')


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'week_day', 'start_time', 'end_time')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'title')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'chairperson_id')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('bldg_initials', 'bldg_name', 'room_num')


class ExtendUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_chairperson', 'is_professor')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(extendUser, ExtendUserAdmin)
