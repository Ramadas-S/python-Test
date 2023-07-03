from django.urls import path
from . import views

urlpatterns = [
    path('',views.short_term_courses,name='short_term_courses'),
    path('short-course-create/',views.short_course_create,name='short_course_create'),
    path('course_delete/<int:pk>',views.course_delete,name='course_delete'),
    path('course_edit/<int:pk>',views.edit_course,name='edit_course'),
    path('',views.update_record,name='update_record'),
    path('search/',views.search,name='search'),
]
