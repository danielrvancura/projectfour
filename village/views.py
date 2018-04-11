from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse
from .models import Child
from .forms import ChildForm, LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import requests

# Create your views here.



def index(request):
    children = Child.objects.all()
    form = ChildForm()
    return render(request, 'index.html', {'children': children, 'form': form})

    #render(request, template, context)

def show(request, child_id):
    child = Child.objects.get(id=child_id)
    return render(request, 'show.html', {'child': child})

def post_child(request):
    form = ChildForm(request.POST)
    if form.is_valid():
        child = form.save(commit = False)
        child.user = request.user
        child.save()
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    children = Child.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'children':children})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password= p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("This account has been disabled")
            else:
                print("The usermane and or password is incorrect")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

# def like_cat(request):
#     cat_id = request.GET.get('cat_id', None)
#     likes = 0
#     if (cat_id):
#         cat = Cat.objects.get(id=int(cat_id))
#         if cat is not None:
#             likes = cat.likes + 1
#             cat.likes = likes
#             cat.save()
#     return HttpResponse(likes)


def edit_child(request, child_id):
    instance = get_object_or_404(Child, id=child_id)
    print(instance.child_name)
    print(instance.affliction)

    form = ChildForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        # form = ChildForm(request.POST)
        if form.is_valid():
            print("FORM IS VALID FORM IS VALID FORM IS VALID FORM IS VALID")
            obj = form.save(commit=False)
            print("This is the submitted child's name:", obj.child_name)
            obj.user = request.user
            obj.save()
        return redirect('show', child_id)
    else:
        print("THIS IS NOT A POST REQUEST")
        return render(request, 'edit_child.html', {'child': instance, 'form': form})


def delete_child(request, child_id):
    if request.method == 'POST':
        instance = Child.objects.get(pk=child_id)
        instance.delete()
        return redirect('index')

#find or create
# def create_toy(request, child_id):
#     form = ToyForm(request.POST)
#     if form.is_valid():
#         try:
#             toy = Toy.objects.get(name=form.data.get('name'))
#         except:
#             toy = None
#         if toy is None:
#             toy = form.save()
#         child = Child.objects.get(pk=child_id)
#         toy.cats.add(cat)
#         return redirect('show_toy', toy.id)
#     else:
#         return redirect('show', cat_id)

# def show_toy(request, toy_id):
#     toy = Toy.objects.get(pk=toy_id)
#     cats = toy.cats.all()
#     return render(request, 'show_toy.html', {'toy': toy, 'cats':cats})
#
# def api(request):
#     payload = {'key': 'Mjk0MTkz'}
#     res = requests.get('http://thecatapi.com/api/images/get', params=payload)
#     return render(request, 'api.html', {'imageurl': res.url})
