from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [

    path('', views.index, name='index'),

    path('contact', views.contact, name='contact'),
    path('courses', views.course, name='course'),
    path('courses/<int:id>/', views.students, name='students'),
    path('courses/schedule', views.schedule_lesson, name='schedule_lesson'),
    path('courses/schedule/delete/<int:pk>/', views.ScheduleLessonDelete.as_view(), name='schedule_delete'),
    path('courses/schedule/<int:pk>/', views.ScheduleLessonUpdate.as_view(), name='schedule_update'),
    path('courses/<int:id>/scheduled', views.scheduled, name='scheduled'),
    path('courses/<int:id>/group_view', views.group_view, name='group_view'),
    path('courses/<int:id>/<int:attd_val>', views.scheduled_attendance, name='scheduled_attendance'),
   # path('courses/<int:id>/<int:attd_val>', views.GroupAttendance.as_view(), name='group_attendance'),
    path('courses/<int:id>/add/', views.add_student, name='add_student'),

    path('student/view/<int:id>', views.student_view, name='student_view'),
    path('student/<int:pk>/', views.StudentUpdate.as_view(), name='student_update'),
    path('student/delete/<int:pk>/', views.StudentDelete.as_view(), name='student_delete'),

    path('course/delete/<int:id>/', views.course_delete, name='course_delete'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),

]
