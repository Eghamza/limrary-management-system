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
         views.edit_register, name='edit_registration'),
    path('edit_students/<id>', views.edit_students, name='edit_students'),
    path('delete_student/<int:id>', views.delete_student, name='delete_student'),
    path('create_group', views.create_group, name='create_group'),
    path('edit_group/<int:id>', views.edit_group, name='edit_group'),
    path('delete_group/<int:id>', views.delete_group, name='delete_group'),
    path('view_group', views.view_group, name='view_group'),

]
