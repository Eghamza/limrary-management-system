
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

    dele = narrow_book.objects.filter(id=id)
    dele.delete()
    messages.info(request, "Book deleted ! ")
    return redirect('/')


@login_required(login_url='login')
def edit(request, id):
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

    if request.method == 'POST':
        bookname = request.POST['name']
        author = request.POST['author']
        qnty = request.POST['qty']

        sbooks = books(name=bookname, auth=author, quantity=qnty)
        sbooks.save()
        messages.info(request, 'Book saved')
        return redirect('/')

    return render(request, 'books.html')


@login_required(login_url='login')
def edit_book(request, id):
    book = books.objects.get(id=id)
    if request.method == 'POST':
        bookname = request.POST['name']
        author = request.POST['author']
        qnty = request.POST['qty']

        sbooks = books(id=id, name=bookname, auth=author, quantity=qnty)
        sbooks.save()
        messages.info(request, 'Book updated')
        return redirect('/')
    return render(request, 'edit_books.html', {'books': book})

def delete_book(request,id):
    book = books.objects.get(id=id)
    book.delete()
    messages.info(request, "Book deleted! ")
    return redirect('/')
