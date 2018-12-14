from django.urls import path
from django.conf.urls import url

from gestionclasse import views as g_views

urlpatterns = [
    path('', g_views.ClassList.as_view(),name='class-list'),
    path('view/<int:pk>/', g_views.ClasseEleveMensualiteList.as_view(),name='class-student-list'),
    path('new',g_views.CreateClass.as_view(),name='new-class'),
    path('delete/<int:pk>/',g_views.DeleteClass.as_view(),name='delete-class'),
    path('update/<int:pk>/',g_views.UpdateClass.as_view(),name='update-class'),
    path('students/new', g_views.CreateStudent.as_view(),name='new-student'),
    path('students/view/<int:pk>/',g_views.SingleStudent.as_view(),name='single-student'), # for read or update
    path('statistics',g_views.statistics,name='statistics')

]
