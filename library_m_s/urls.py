from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),

    path('new-book', views.book, name='new-book'),
    path('edit/<id>', views.edit, name='edit'),
    path('delete/<id>', views.delete_book, name='delete'),
    path('edit_book/<id>', views.edit_book, name='edit_book'),
    path('delete_book/<id>', views.delete_book, name='delete_book'),
    path('view_book', views.view_book, name='view_book'),
    path('view_barrow', views.view_barrow, name='view_barrow'),
    path('view_client', views.view_client, name='view_client'),
    
    # path('',views.login_user,name='login_user'),

    # path('register',views.register,name='register')

]
