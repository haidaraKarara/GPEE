from django.urls import path
from django.conf.urls import url

from gestionclasse import views as g_views

urlpatterns = [
    path('classe/liste', g_views.ClasseList.as_view(),name='liste-classes'),
    path('classe/liste-eleves/<int:pk>/', g_views.ClasseEleveList.as_view(),name='liste-eleves-classe'),
    path('eleve/nouveau/', g_views.CreateEleve.as_view(),name='nouveau-eleve'),

]
