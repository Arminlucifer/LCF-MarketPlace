from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import EditProfile
from base.models import Product
from . models import User
from account.forms import MyUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from base.models import Product
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def loginuser(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

    try:
        user = User.objects.get(email=email)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or password is incorrect!')
    except User.DoesNotExist:
        messages.error(request, 'Email does not Exist!')
    except Exception as e:
        messages.error(request, f'An error occured: {e}')
    context = {'page': page}
    return render(request, 'account/login-register.html', context)


def logoutuser(request):
    logout(request)
    return redirect('home')


def registeruser(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                user = form.save(commit=False)
                user.username = form.cleaned_data.get('username')
                user.email = form.cleaned_data.get('email')
                user.save()
                login(request, user)
                return redirect('home')

        except Exception as e:
            messages.error(request, f'An error occured: {e}')

    context = {'form': form}
    return render(request, 'account/login-register.html', context)


def profile(request, username):
    page = 'profile'
    user = User.objects.get(username=username)

    products = user.product_set.all()
    products_count = products.count()

    print(products_count)

    print(products)

    context = {'user': user, 'page': page,
               "products_count": products_count, "products": products}

    return render(request, 'base/home.html', context)


@login_required(login_url='login')
def editprofile(request, username):

    user = User.objects.get(username=username)

    if request.user.id != user.id:
        messages.error(request, 'You Cannot Edit This Profile! ')
        return redirect('home')

    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully! 🎉')
            return redirect('home')
        else:
            messages.error(
                request, 'Failed to update profile. Please check the form.')
    else:
        form = EditProfile(instance=user)

    context = {"form": form, "profile_user": user}
    return render(request, 'account/edit_profile.html', context)
