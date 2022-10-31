from genericpath import exists
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm
from home.models import User, MyUser

# Create your views here.
def createUser(request):
    Name = request.POST.get('Name')
    Description = request.POST.get('Description')
    Married = request.POST.get('Married')
    Birthday = request.POST.get('Birthday')
    Image = request.POST.get('Image')

    order = User.objects.all()
    form = UserForm()
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'order': order}
    return render(request, 'index.html', context)

def updateUser(request, pk):
    order = User.objects.get(id=pk)
    form = UserForm()
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = UserForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'order': order}
    return render(request, 'update.html', context)

def deleteUser(request, pk):
    order = User.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'Item': order}
    return render(request, 'delete.html', context)



# def signup(request):
#     order = MyUser.objects.all()
#     form = MyUserForm()
#     if request.method == 'POST':
#         print(request.POST, request.FILES)
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form': form, 'order': order}
#     return render(request, 'signup.html', context)