from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-attr'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address', 'class': 'form-attr'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Message Title', 'class': 'form-attr'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message goes here . . .', 'class': 'form-attr'}))

    class Meta:
        model = Contact
        exclude = ('created', 'updated')

    def clean(self):
        super(ContactForm, self).clean()

        first_name = self.cleaned_data.get('first_name')
        email = self.cleaned_data.get('email')
        title = self.cleaned_data.get('title')
        message = self.cleaned_data.get('message')

        return self.cleaned_data


class CourseForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Create new course ...'}))

    class Meta:
        model = Class
        fields = ['name', ]

    def clean(self):
        cleaned_data = super(CourseForm, self).clean()
        name = cleaned_data.get('name')

        return cleaned_data


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone', 'class_name']


class ScheduleLessonUpdateForm(forms.ModelForm):
    class Meta:
        model = ScheduleLesson
        fields = ['course', 'datetime']
        labels = {
            'course': '',
            'datetime': '',

        }


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone', 'class_name']
        labels = {
            'first_name': '',
            'middle_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
            'class_name': '',
        }


class ScheduleLessonForm(forms.ModelForm):
    class Meta:
        model = ScheduleLesson
        fields = ['course', 'datetime']
        labels = {
            'course': '',
            'datetime': ''
        }


class GroupAttendanceForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='',
        queryset=Student.objects.all()
    )

    class Meta:
        model = GroupAttendance
        fields = ['scheduled_lesson', 'students']
