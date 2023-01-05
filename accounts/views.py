from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

from library_m_s.models import books, student, narrow_book


@login_required(login_url='login')
def membership(request):
    book = books.objects.all()

    s_user = student.objects.all()
    if request.method == 'POST':
        user_email = request.POST['user']
        start_d = request.POST['start_date']
        end_d = request.POST['end_date']
        book = request.POST['book1']
        # try:
        #     membership = narrow_book.objects.get(narrow_book.student.email=user_email)
        # except narrow_book.DoesNotExist:
        #     membership = None
        mem = narrow_book(start_date=start_d, end_date=end_d,
                          book_id=book, student_id=user_email)
        mem.save()
        messages.info(
            request, 'success fully membeship created f"{user_email}".')
        return redirect('/')

    return render(request, 'member.html', {'books': book, 'usrs': s_user})


def loginu(request):
    if request.user.is_authenticated:
        messages.info(request, 'alredy login')
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                messages.info(request, 'wellcame Administrator')
            #     return redirect('./admin')
            else:
                messages.info(request, 'Hello  wellcame ', username)
            return redirect("/")

        else:
            if request.user.is_active:
                messages.info(request, 'user or password is incorrect')

            else:
                messages.info(
                    request, 'This user is not active please contact the administrator')

    return render(request, 'loginu.html')


@login_required(login_url='login')
def user_register(request):
    result = books.objects.all()
    if request.method == 'POST':

        fneme = request.POST['frist_name']
        mname = request.POST['middel_name']
        lname = request.POST['last_name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']

        rg = student(fname=fneme, address=address, lname=lname,
                     mname=mname, phone=phone, email=email)
        rg.save()
        messages.info(request, 'successfull Register ')
        return redirect('/')
    else:
        print("nothing is going")

    return render(request, 'user_register.html', {'blist': result})
# Create your views here.


@login_required(login_url='login')
def log_out(request):
    logout(request)
    messages.info(request, 'logout')
    return render(request, 'loginu.html')


@login_required(login_url='login')
def admin(request):
    return render(request, 'admin1.html')


@login_required(login_url='login')
def staff_register(request):

    if request.method == 'POST':
        fneme = request.POST['first_name']
        username = request.POST['username']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        active = request.POST['active']
        superuser = request.POST['superuser']
        staff = request.POST['staff']
        rg = User.objects.create_user(first_name=fneme, last_name=lname, username=username, email=email,
                                      password=password, is_staff=staff, is_active=active, is_superuser=superuser)
        rg.save()
        messages.info(request, 'successfull Register ')
        return redirect('/')

    return render(request, 'staff_registration.html')


@login_required(login_url='login')
def edit_register(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        fneme = request.POST['first_name']
        username = request.POST['username']
        lname = request.POST['last_name']

        email = request.POST['email']
        password = request.POST['password']
        active = request.POST['active']
        superuser = request.POST['superuser']
        staff = request.POST['staff']
        rg = User.objects.create_user(id=id, first_name=fneme, last_name=lname, username=username, email=email,
                                      password=password, is_staff=staff, is_active=active, is_superuser=superuser)
        rg.save()
        messages.info(request, 'successfull Edit ')
        return redirect('/')
    return render(request, 'edit_registration.html', {'user': user})
