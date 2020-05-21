from django.shortcuts import render
from poll.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def pollsList(request):
    questions = Question.objects.all()
    context = { 'title':'polls', 'questions':questions }
    return render(request, 'poll/index.html', context)


# def pollDetails(request, id):
#     question = Question.objects.get(id=id)
#     context = { 'question':question }
#     return render(request, 'poll/details.html', context)



@login_required(login_url="user-login")
def poll(request, id=None):
    if request.method == 'GET':
        question = Question.objects.get(id=id)
        context = { 'question':question }
        return render(request, 'poll/poll.html', context)

    if request.method == 'POST':
        user_id = request.user.id        # It is used to get the login user
        data = request.POST['choice']
        ret = Answer.objects.create(user_id=user_id, choice_id=data)
        if ret:
            return HttpResponseRedirect(reverse('polls-list'))
        else:
            return HttpResponse("Not Created")

 