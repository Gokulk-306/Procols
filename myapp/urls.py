from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name="index"),
    path('register/',views.register, name="register"),
    path('reviews/',views.contact,name='reviews'),
    path('about/',views.about,name='about'),
    path('student-call/', views.StudentCallList, name='student_call'),


]