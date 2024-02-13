from Auth.forms import UserForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import models
from .forms import FormTransaction, FormCustomer 

def index(request):   
    return render(request, 'index.html')

# Регистрация аккаунта
def register(request):
    if request.method == "POST":
        form_register = UserForm(request.POST)
        if form_register.is_valid():
            user = form_register.save(commit=False)
            user.set_password(user.password)
            form_register.save()
            
            return redirect('index')
        else:
            return redirect('register')
    else:
        form_register = UserForm()
    return render(request, 'register.html', {'form_register': form_register})


# Вход аккаунта
def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 

        if username and password:
            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли!')
                    return redirect('index')
                else:    
                    messages.error(request, 'Неверный логин или пароль!')
            except Exception as ex:
                messages.error(request, 'Произошла ошибка при аутентификации. Пожалуйста, попробуйте снова')
        else:
            messages.warning(request, 'Заполните все поля!')
    else:
        return render(request, 'auth.html')
    

# Выход из аккаунта
def exit(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли!')
    return redirect('index')



# Транзакции
def transaction(request):
    if request.method == 'POST':
        transaction = FormTransaction(request.POST, request.FILES)
        if transaction.is_valid():
            transaction.save()
            return redirect('transaction')
    else:
        transaction = FormTransaction()
        context = {
            'transaction': transaction,
        }
        return render(request, 'transaction.html', context)