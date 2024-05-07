from django.contrib.auth import views as auth_views
from django.urls import path


from .views import *


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='usuariologs/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
]