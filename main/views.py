from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from .forms import *
from .models import *


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            post = contact_form.save(commit=False)
            post.save()
            print("Success!")
            return render(request, 'main/index.html')
        else:
            return render(request, "main/contact.html", {'form': contact_form})
    else:
        form = ContactForm(None)
    return render(request, 'main/contact.html', {'form': form})


def about(request):
    return render(request, 'main/about_company.html', context={})


# @login_required
def course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:course')
        else:
            raise ValidationError('Form is not valid.')
    else:
        form = CourseForm()

    all_courses = Class.objects.all()

    context = {
        'form': CourseForm,
        'all_courses': all_courses,
    }

    return render(request, 'main/class.html', context)


# @login_required
def course_delete(request, id):
    obj = get_object_or_404(Class, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('main:course')

    context = {'course': obj}
    return render(request, 'main/course_delete.html', context)


def add_student(request, id):
    course = get_object_or_404(Class, id=id)
    if request.method == 'POST':
        form = AddStudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('main:students', id)
        else:
            raise ValidationError('Form is not valid.')
    else:
        form = AddStudentForm()

    context = {
        'form': form,
        'course': course,
        'id': id
    }
    return render(request, 'main/add_student.html', context)


def students(request, id):
    class_name = get_object_or_404(Class, id=id)
    students = Student.objects.filter(class_name=class_name)

    context = {'students': students, 'course': class_name}
    return render(request, 'main/students.html', context)


def group_view(request, id):
    course_name = get_object_or_404(Class, id=id)

    all_students = Student.objects.filter(class_name=course_name)
    group1 = all_students[:len(all_students) // 2]
    group2 = all_students[len(all_students) // 2:]
    context = {'course': course_name, 'group1': group1, 'group2': group2}
    return render(request, 'main/group_view.html', context)


def schedule_lesson(request):
    if request.method == 'POST':
        form = ScheduleLessonForm(request.POST)

        if form.is_valid():
            course = request.POST.get('course')
            print("Hello", course)
            form.save()
            return redirect('main:scheduled', course)
        else:
            raise ValidationError('Form is not valid.')
    else:
        form = ScheduleLessonForm()
    return render(request, 'main/schedule_lesson.html', context={'form': form, })


def scheduled(request, id):
    course_name = get_object_or_404(Class, id=id)
    all_scheduled_lessons = ScheduleLesson.objects.filter(course=course_name)

    context = {
        'course': course_name,

        'lessons': all_scheduled_lessons
    }
    return render(request, 'main/booked_lessons.html', context)


def student_view(request, id):
    student = get_object_or_404(Student, id=id)
    all_attendance = StudentAttendance.objects.filter(student=student)
    all_weeks = Attendance.objects.all()
    attended_weeks = list()
    for b in all_attendance:
        attended_weeks.append(b.attended.title)
    context = {'student': student, 'attended_weeks': attended_weeks, 'all_weeks': all_weeks}
    return render(request, 'main/student_view.html', context)


class StudentUpdate(UpdateView):
    model = Student
    template_name = "main/student_edit.html"
    context_object_name = 'student'
    form_class = StudentForm

    def get_context_data(self, *args, **kwargs):
        context = super(StudentUpdate, self).get_context_data(*args, **kwargs)
        context['all_weeks'] = Attendance.objects.all()
        all_attendance = StudentAttendance.objects.filter(student=context['student'])
        attended_weeks = list()
        for b in all_attendance:
            attended_weeks.append(b.attended.title)
        context['attended_weeks'] = attended_weeks
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:student_view', kwargs={'id': self.kwargs['pk']})


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy("main:index")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ScheduleLessonDelete(DeleteView):
    model = ScheduleLesson
    success_url = reverse_lazy("main:course")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def scheduled_attendance(request, id, attd_val):
    course_name = get_object_or_404(Class, id=id)
    schedule = get_object_or_404(ScheduleLesson, id=attd_val)
    all_students = Student.objects.filter(class_name=course_name)
    all_weeks = Attendance.objects.all()
    group1 = all_students[:len(all_students) // 2]
    group2 = all_students[len(all_students) // 2:]

    if attd_val % 2 == 0:
        lesson_type = 'online'
    else:
        lesson_type = 'offline'

    context = {
        'course': course_name,

        'lesson_type': lesson_type,
        'group1': group1,
        'group2': group2,
        'schedule': schedule,
        'all_weeks': all_weeks
    }
    return render(request, 'main/scheduled_attendance.html', context)


# is not used. Test & Debugging failed. Instead `scheduled_attendance` function is used.
class GroupAttendance(CreateView):
    model = GroupAttendance
    form_class = GroupAttendanceForm
    template_name = 'main/group_attendance.html'
    success_url = reverse_lazy('main:course')

    def get_context_data(self, *args, **kwargs):
        context = super(GroupAttendance, self).get_context_data(*args, **kwargs)
        context['all_weeks'] = Attendance.objects.all()
        context['course'] = get_object_or_404(Class, id=self.kwargs['id'])
        context['schedule'] = get_object_or_404(ScheduleLesson, id=self.kwargs['attd_val'])

        return context

    def get_queryset(self):
        students = self.kwargs.get('students')

        queryset = Student.objects.filter(class_name=Class.objects.filter(id=self.kwargs['attd_val']))
        return queryset


class ScheduleLessonUpdate(UpdateView):
    model = ScheduleLesson
    template_name = "main/scheduled_edit.html"
    context_object_name = 'lesson'
    form_class = ScheduleLessonUpdateForm
    success_url = reverse_lazy("main:course")


def login(request):
    return render(request, 'account/login.html', context={})


def signup(request):
    return render(request, 'account/signup.html', context={})
