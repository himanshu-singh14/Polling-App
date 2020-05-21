from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from employee.forms import UserForm
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView



@login_required(login_url="user-login")
def EmployeeList(request):
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Employees'
    return render(request, 'employee/index.html', context)



def EmployeeDetails(request, id=None):
    context = {}
    context['user'] = get_object_or_404(User, id=id)
    return render(request, 'employee/details.html', context)



def EmployeeEdit(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee-list'))
        else:
            return render(request, 'employee/edit.html', {'user_form': user_form})
    else:
        if request.user.id == user.id:
            user_form = UserForm(instance=user)
            return render(request, 'employee/edit.html' , {'user_form': user_form})
        else:
            return HttpResponseRedirect(reverse('employee-list'))



def EmployeeAdd(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee-list'))
        else:
            return render(request, 'employee/add.html', {'user_form': user_form})
    else:
        user_form = UserForm()
        return render(request, 'employee/add.html' , {'user_form': user_form})



def EmployeeDelete(request, id=None):
    user = get_object_or_404(User, id=id)
    context = {}
    context['user'] = user
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('employee-list'))
    else:
        return render(request, 'employee/delete.html', context)



def UserLogin(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):          # It is important
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('polls-list'))
        else:
            context['error'] = 'Please provide valid credentials !!'
            return render(request, 'employee/login.html', context)
    else:
        return render(request, 'employee/login.html', context)



# def Success(request):
#     context = {}
#     context['user'] = request.user
#     return render(request, 'employee/success.html', context)



def UserLogout(request):
    if request.method == 'POST':
        print(request)
        logout(request)
        return HttpResponseRedirect(reverse('polls-list'))



class MyProfile(DetailView):
    template_name = 'employee/profile.html'

    def get_object(self):
        return self.request.user.profile # This will return object of profile object
                                         # This will send object_list if it was ListView



class ProfileUpdate(UpdateView):
    fields = ['designation', 'salary']
    template_name = 'employee/profile_update.html'
    success_url = reverse_lazy('my-profile')

    def get_object(self):
        return self.request.user.profile
