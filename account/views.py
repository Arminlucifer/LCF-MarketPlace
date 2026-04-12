from django.shortcuts import render, redirect
from . models import User
from account.forms import MyUserCreationForm
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages

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
                messages.error(request,f'An error occured: {e}')
        context = {'page':page}
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

        context = {'form':form}
        return render(request, 'account/login-register.html', context)