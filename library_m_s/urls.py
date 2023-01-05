from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),

    path('new-book', views.book, name='new-book'),
    path('edit/<id>', views.edit, name='edit'),
    path('delete/<id>', views.delete_book, name='delete'),
    path('edit_book/<id>', views.edit_book, name='edit_book'),
    path('delete_book/<id>', views.delete_book, name='delete_book'),
    # path('',views.login_user,name='login_user'),

    # path('register',views.register,name='register')

]
