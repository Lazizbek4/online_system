from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=64)
    available = models.BooleanField(default=True)
    created = models.DateTimeField("Created", auto_now_add="True")
    updated = models.DateTimeField("Updated", auto_now="True")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "All Classes"


class LessonType(models.Model):
    choice = models.CharField(max_length=16)

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = "Lesson Type"
        verbose_name_plural = "Lesson Types"


class Attendance(models.Model):
    choices = [
        # X -> absent, O -> absent
        ('X', 'X'),
        ('O', 'O')
    ]
    title = models.CharField(max_length=16)
    attendance = models.CharField(max_length=8, default='X', choices=choices)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Attendance Weeks"
        verbose_name_plural = "Attendance Weeks"


class Groups(models.Model):
    group_num = models.CharField(max_length=32, default='Unknown')

    def __str__(self):
        return str(self.group_num)

    class Meta:
        verbose_name = "Groups"
        verbose_name_plural = "Groups"


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=16)
    class_name = models.ForeignKey(Class, default='Unknown', on_delete=models.CASCADE)

    # group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "All Students"


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attended = models.ForeignKey(Attendance, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.attended)

    class Meta:
        verbose_name = "Student Attendance"
        verbose_name_plural = "Student Attendance"


class Contact(models.Model):
    first_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    title = models.CharField(max_length=64)
    message = models.TextField(max_length=1000)
    created = models.DateTimeField("Date Creation", auto_now_add="True")
    updated = models.DateTimeField("Date Modification", auto_now="True")

    class Meta:
        verbose_name = "Contact Request"
        verbose_name_plural = "Contact Requests"


class ScheduleLesson(models.Model):
    course = models.ForeignKey(Class, on_delete=models.CASCADE, default='')
    datetime = models.DateTimeField("Schedule Date")
    created = models.DateTimeField("Created", auto_now_add="True")
    updated = models.DateTimeField("Updated", auto_now="True")

    def __str__(self):
        return str(self.course)

    class Meta:
        verbose_name = "Scheduled Lesson"
        verbose_name_plural = "Scheduled Lessons"


class GroupAttendance(models.Model):
    scheduled_lesson = models.ForeignKey(ScheduleLesson, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    attendance_week = models.ForeignKey(Attendance, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField("Created", auto_now_add="True")
    updated = models.DateTimeField("Updated", auto_now="True")

    def __str__(self):
        return str(self.scheduled_lesson)

    class Meta:
        verbose_name = "Group Attendance"
        verbose_name_plural = "Group Attendance"
