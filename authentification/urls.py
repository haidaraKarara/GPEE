from django.urls import path
from django.conf.urls import url

from authentification import views as con_views

urlpatterns = [
    path('auth/login', con_views.login),
    path('auth/logout',con_views.logout_view),
]
