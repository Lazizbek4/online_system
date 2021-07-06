from django.contrib import admin

from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'title', 'created',)
    list_filter = ('first_name', 'created')
    search_fields = ['first_name', ]


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'updated', 'created')
    list_filter = ('name',)
    search_fields = ['name', ]


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'attendance',)


class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'attended',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'class_name',)
    list_filter = ('first_name', 'last_name', 'email', 'phone',)
    search_fields = ['first_name', 'last_name', 'email', 'phone', ]


# class GroupsAdmin(admin.ModelAdmin):
#     list_display = ('group_num',)

class ScheduleLessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'datetime', 'created', 'updated')


class GroupAttendanceAdmin(admin.ModelAdmin):
    list_display = ('scheduled_lesson', 'created', 'updated')


class LessonTypeAdmin(admin.ModelAdmin):
    list_display = ('choice',)
    list_filter = ('choice',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Class, ClassAdmin)
# admin.site.register(GroupAttendance, GroupAttendanceAdmin)
admin.site.register(ScheduleLesson, ScheduleLessonAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(StudentAttendance, StudentAttendanceAdmin)
admin.site.register(LessonType, LessonTypeAdmin)
admin.site.register(Student, StudentAdmin)
