from django.urls import path
from django.conf.urls import url, include

from authentification import views as con_views
from knox import views as knox_views

urlpatterns = [
    # url(r'api/auth/', include('knox.urls'))
    # url(r'login/', con_views.LoginView.as_view(), name='knox_login'),
    # url(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    # url(r'logoutall/', knox_views.LogoutAllView.as_view(permission_classes = (permissions.AllowAny,)), name='knox_logoutall'),
]
