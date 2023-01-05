from django.urls import path
from . import views
urlpatterns = [
    path('login', views.loginu, name='login'),
    path('logout', views.log_out, name='logout'),
    path('register', views.user_register, name='register'),
    path('membership', views.membership, name='membership'),
    path('admin', views.admin, name='admin'),
    path('staff_register', views.staff_register, name='staff_register'),
    path('edit_registration/<int:id>',
         views.edit_register, name='edit_registration')


]
