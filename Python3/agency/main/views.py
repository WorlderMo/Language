from django.shortcuts import render

# Create your views here.
from users.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import orderInfo

def index(request):
    return render(request, 'index.html')


def sign_in(request):
    return render(request, 'login.html')


def sign_up(request):
    return render(request, 'register.html')

def order(request):
    return render(request,'goodsMessages.html')


def registerUserMessage(request):
    if request.method == 'POST':
        realName = request.POST['realName']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(realName=realName, email=email, password=password)
        # user.name = name
        # user.email = email
        # user.password = password
        user.save()
        return render(request, 'login.html')
    return HttpResponse("请输入正确的格式")

def longinVerify(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'index.html')
        else:
            return HttpResponse('用户名或者密码错误')


def orderMessages(request):
    if request.method == 'POST':
        customerName=request.POST['customerName']
        customerPhone=request.POST['customerPhone']
        customerAddress=request.POST['customerAddress']
        orderName=request.POST['orderName']

        indent=orderInfo.objects.create(customerName=customerName,customerPhone=customerPhone,customerAddress=customerAddress,orderName=orderName)
        indent.save()

        return HttpResponse("提交成功")
    return HttpResponse("请争取提交")