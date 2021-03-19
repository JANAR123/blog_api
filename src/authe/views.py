from django.shortcuts import render,redirect
from .forms import AuthorForm,LoginForm
from .models import Author,ConfirmCode
from .utils  import send_to_mail
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout

# Create your views here.

def author_form(request):
    form=AuthorForm()
    if request.method=='POST':
        save_form=AuthorForm(request.POST)
        if save_form.is_valid():
            author=Author(username=request.POST['username'],email=request.POST['email'])
            author.set_password(request.POST['password'])
            author.save()
            code= ConfirmCode.objects.create(author=author)
            send_to_mail(author.email,code.code)
            message = "Все ок"
            return render(request,'reply.html',{"message":message})
        elif Author.objects.filter(email=request.POST['email'],verified=False) or Author.objects.filter(verified=False,username=request.POST['username']):
            author=None
            if Author.objects.filter(email=request.POST["email"]):
                author=Author.objects.get(email=request.POST["email"])
            elif Author.objects.filter(username=request.POST['username']):
                author=Author.objects.get(username=request.POST['username'])  
            code= ConfirmCode.objects.create(author=author)
            send_to_mail(author.email,code.code)
            message = "Все ок"
            return render(request,'reply.html',{"message":message})      
        message=save_form.errors
        return render(request,'reply.html',{"message":message})    
    return render(request,'register.html',{'form':form})


def confirm_email(request,code):
    code=ConfirmCode.objects.filter(code=code)
    message="Ваш код не верен"
    if code:
        if not code.last().confirm:
            code=code.last()
            code.confirm=True
            code.save()
            author=code.author
            author.verified=True
            author.save()
            message="Ваша почта подверждена"
    return render(request,'reply.html',{"message":message})


def login(request):
    form=LoginForm()
    if request.method=='POST':
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user:
            auth_login(request,user)
            return render(request,'reply.html',{"message":"Вы зашли","success":True})
        return render(request,'reply.html',{"message":"Такой пользователь не найден ","success":True})    
    return render(request,'login.html',{"form":form})


def logout_views(request):
    logout(request)
    return redirect("api:post_html")

