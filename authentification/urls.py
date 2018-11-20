from django.urls import path
from django.conf.urls import url

from authentification import views as con_views

urlpatterns = [
    path('api/login', con_views.login),
    path('api/logout',con_views.logout_view),
]
