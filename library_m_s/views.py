
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import books, student, narrow_book, books
from django.contrib.auth import authenticate, login, get_user_model
from datetime import datetime, date
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
# delete


@login_required(login_url='login')
def delete_book(request, id):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        dele = narrow_book.objects.filter(id=id)
        dele.delete()
        messages.info(request, "Book deleted ! ")
        return redirect('/')
    else:
        return redirect('login')


@login_required(login_url='login')
def edit(request, id):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        context = {
            'nbook': narrow_book.objects.get(id=id),
            'book': books.objects.all()
        }

        if request.method == 'POST':

            email = request.POST['user']
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            book_name = request.POST['book1']
            nb = narrow_book(id=id, student_id=email, start_date=start_date,
                             end_date=end_date, book_id=book_name)
            nb.save()
            return redirect('home')
    else:
        return redirect('login')
    return render(request, 'edit_u.html', context)


@login_required(login_url='login')
def home(request):
    bks = books.objects.all()
    students = student.objects.all()
    nbooks = narrow_book.objects.all()
    user = get_user_model()
    users = user.objects.all()
    now = date.today()
    return render(request, 'home.html', {'students': students, 'now': now, 'books': nbooks, 'users': users, 'bks': bks})


@login_required(login_url='login')
def book(request):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        if request.method == 'POST':
            bookname = request.POST['name']
            author = request.POST['author']
            qnty = request.POST['qty']
            sbooks = books(name=bookname, auth=author, quantity=qnty)
            sbooks.save()
            messages.info(request, 'Book saved')
            return redirect('/')
    else:
        return redirect('login')

    return render(request, 'books.html')


@login_required(login_url='login')
def edit_book(request, id):
    book = books.objects.get(id=id)
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        if request.method == 'POST':
            bookname = request.POST['name']
            author = request.POST['author']
            qnty = request.POST['qty']

            sbooks = books(id=id, name=bookname, auth=author, quantity=qnty)
            sbooks.save()
            messages.info(request, 'Book updated')
            return redirect('edit_book')
    else:
        return redirect('login')
    return render(request, 'edit_books.html', {'books': book})


@login_required(login_url='login')
def delete_book(request, id):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        book = books.objects.get(id=id)
        book.delete()
        messages.info(request, "Book deleted! ")
        return redirect('/')
    else:
        return redirect('login')


@login_required(login_url='login')
def view_book(request):
    bks = books.objects.all()
    return render(request, 'view_book.html', {'bks': bks})


@login_required(login_url='login')
def view_barrow(request):
    nbooks = narrow_book.objects.all()
    return render(request, 'view_barrow.html', {'books': nbooks})


@login_required(login_url='login')
def view_client(request):
    students = student.objects.all()
    return render(request, 'view_client.html', {'students': students})


    students = student.objects.get(id=id)
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        if request.method == 'POST':

            student_id = request.POST['student_id']