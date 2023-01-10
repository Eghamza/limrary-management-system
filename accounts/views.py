from django.contrib import messages
from django import template
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from .form import groupForm
from library_m_s.models import books, student, narrow_book

# membership


@login_required(login_url='login')
def membership(request):
    bookall = books.objects.all()

    s_user = student.objects.all()

    if request.method == 'POST':
        user_email = request.POST['user']
        start_d = request.POST['start_date']
        end_d = request.POST['end_date']
        book = request.POST['book1']
        geted_book = books.objects.get(id=book)
        geted_user = student.objects.get(id=user_email)
        usermail = geted_user.id

        bk = geted_book.id
        qty = geted_book.quantity
        if qty <= 5:

            messages.info(request, 'this book is out of library')
        else:
            # checkbook=
            if narrow_book.objects.filter(student=usermail, book=bk):
                messages.info(request, 'you have already been assigned')
            else:
                mem = narrow_book(start_date=start_d, end_date=end_d,
                                  book_id=book, student_id=user_email)
                mem.save()
                geted_book.quantity = qty - 1
                geted_book.save()
                messages.info(
                    request, 'success fully membeship created.')
                return redirect('/')
    return render(request, 'member.html', {'books': bookall, 'usrs': s_user})

# login


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

# client registration


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
# logout user


@login_required(login_url='login')
def log_out(request):
    logout(request)
    messages.info(request, 'logout')
    return render(request, 'loginu.html')
# admin


@login_required(login_url='login')
def admin(request):
    return render(request, 'admin1.html')
# staff registration


@login_required(login_url='login')
def staff_register(request):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        gp = Group.objects.all()

        if request.method == 'POST':
            fneme = request.POST['first_name']
            username = request.POST['username']
            lname = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            active = request.POST['active']
            superuser = request.POST['superuser']
            staff = request.POST['staff']
            gruop_id = request.POST['group_id']
            confimpassoword = request.POST['confimpassoword']
            if confimpassoword !=password:
                messages.info(request, 'password not match')
            else:    
                group = Group.objects.get(id=gruop_id)

                rg = User.objects.create_user(first_name=fneme, last_name=lname, username=username, email=email,
                                            password=password, is_staff=staff, is_active=active, is_superuser=superuser)
                rg.save()
                rg.groups.add(group)
                messages.info(request, 'successfull Register ')
                return redirect('/')
    else:
        return redirect('login')

    return render(request, 'staff_registration.html', {'groups': gp})
# edit staff_registration


@login_required(login_url='login')
def edit_register(request, id):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        user1 = User.objects.get(id=id)
        user = User.objects.filter(pk=id)
        grps = Group.objects.filter(user__id__in=user)
        get_grop = []
        for i in grps:
            get_grop.append(i.name)

        grp = Group.objects.all()
        if request.method == 'POST':
            fneme = request.POST['first_name']
            username = request.POST['username']
            lname = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            active = request.POST['active']
            superuser = request.POST['superuser']
            staff = request.POST['staff']
            group_name = request.POST.getlist('Group')

            rg = User.objects.create_user(id=id, first_name=fneme, last_name=lname, username=username, email=email,
                                          password=password, is_staff=staff, is_active=active, is_superuser=superuser)
            rg.save()
            for gname in group_name:
                if gname == group_name:

                    rg.groups.remove(gname)

                rg.groups.add(gname)
                messages.info(request, 'successfull Edit ')
                return redirect('home')

    else:
        return redirect('login')
    return render(request, 'edit_registration.html', {'user': user1, 'group': grps, 'groups': grp})


@ login_required(login_url='login')
def edit_students(request, id):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        students = student.objects.get(id=id)

    if request.method == 'POST':

        fneme = request.POST['frist_name']
        mname = request.POST['middel_name']
        lname = request.POST['last_name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']

        rg = student(id=id, fname=fneme, address=address, lname=lname,
                     mname=mname, phone=phone, email=email)
        rg.save()
        messages.info(request, 'successfull Edited')
        return redirect('/')
    else:
        print("nothing is going")

    return render(request, 'edit_student.html', {'students': students})


@login_required(login_url='login')
def delete_student(request, id):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        students = student.objects.get(id=id)
        students.delete()
        messages.info(request, 'successfull Delete')
        return redirect('/')


@login_required(login_url='login')
def create_group(request):
    group = Group.objects.all()
    if request.method == 'POST':
        name = request.POST['gname']
        check = request.POST.getlist('check')
        # for creating groups
        gr = Group.objects.create(name=name)
        gr.save()

# create group with permissions
        for checks in check:
            perms = Permission.objects.get(id=checks)
            gr.permissions.add(perms)
            gr.save()

        # gpermissions = Group.objects.

        messages.info(request, 'successfull Create Group')
        return redirect('/')
    else:
        form = groupForm

    return render(request, 'create_group.html', {'form': form, 'group': group})


@login_required(login_url='login')
def edit_group(request, id):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        group = Group.objects.filter(id=id)
        group_name = Group.objects.get(id=id)

        perm_list = []

        permis = Permission.objects.filter(group__id__in=group)
        for perm in permis:
            perm_list.append(perm.id)
        if request.method == 'POST':
            name = request.POST['gname']
            checkb = request.POST.getlist('check')
            # for creating groups
            group_per = Group(id=id, name=name)
            group_per.save()
            for ch in checkb:
                perms = Permission.objects.get(id=ch)
                group_per.permissions.add(perms)

            messages.info(request, 'successfull Edit Group')

        return render(request, 'group.html', {'prems': perm_list, 'group': group_name})


@login_required(login_url='login')
def delete_group(request, id):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        group = Group.objects.get(id=id)
        group.delete()
        messages.info(request, 'successfull Delete')
        return redirect('/')


@login_required(login_url='login')
def view_group(request):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        groups = Group.objects.all()
    return render(request, 'view_group.html', {'groups': groups})


register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False
