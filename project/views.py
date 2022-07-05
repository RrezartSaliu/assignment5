from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from project.models import Account, Question


def index(request):
    return render(request, 'index.html', context={"user": request.user})


def login_sign(request):
    return render(request, 'log-sign.html', context={"user": request.user})


def services(request):
    return render(request, 'services.html', context={"user": request.user})


def register(request):
    username = request.POST['user-sign']
    email = request.POST['email-sign']
    password = request.POST['pass-sign']
    if User.objects.filter(username=username) or User.objects.filter(email=email):
        messages.success(request, "Username or email already exists")
        return redirect("/login_sign")
    else:
        user = User.objects.create_user(username, email, password)
        account = Account(user=user, taken_test=0)
        account.save()
        messages.error(request, "You signed up successfully")
        return redirect("/login_sign")


def loginuser(request):
    username = request.POST['user-log']
    password = request.POST['pass-log']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/services')
    else:
        messages.success(request, "The entered information are not correct")
        return redirect("/login_sign")


def logoutuser(request):
    logout(request)
    return redirect("/login_sign")


def quiz(request):
    if request.user.is_anonymous:
        messages.success(request, "You should login first")
        return redirect('/login_sign')

    questions = Question.objects.all()
    questions = questions.order_by('?')[:10]
    return render(request, 'quiz.html', context={"questions": questions})


def submit_test(request):
    correct = 0
    for i in range(10):
        i = i+1
        thestring = 'question_' + str(i)
        question_id = request.GET[thestring].split('_')[0]
        answer_option = request.GET[thestring].split('_')[1]
        print(Question.objects.get(pk=question_id).correct == answer_option)
        if Question.objects.get(pk=question_id).correct == answer_option:
            correct = correct + 1
    toIncTest = Account.objects.get(user=request.user)
    toIncTest.taken_test = toIncTest.taken_test + 1
    toIncTest.save()
    text = "You got " + str(correct) + " out of 10, You have taken " + str(toIncTest.taken_test) + " tests"
    messages.success(request, text)
    return redirect('/services')
