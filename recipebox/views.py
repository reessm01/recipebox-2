from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout

from recipebox.models import Author, Recipe, User
from recipebox.forms import RecipeForm, AuthorForm, SignupForm, LoginForm

def index(request, *args, **kwargs):

    html = "main.html"

    items = Recipe.objects.all()

    return render(request, html, {'stories': items})

def recipeurl(request, id):

    html = "recipe.html"

    items = Recipe.objects.get(id=id)

    return render(request, html, {'stories': items})

def authorurl(request, id):

    html = "author.html"

    items = Recipe.objects.filter(author=id)

    return render(request, html, {'stories': items})

@login_required()
def add_recipe(request, *args, **kwargs):
    html = 'addrecipe.html'

    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = RecipeForm()

    return render(request,html,{'form': form})

@staff_member_required
def add_author(request, *args, **kwargs):
    html = 'addauthor.html'

    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            Author.objects.create(
                user=user,
                name=data['name'],
                bio=data['bio'],
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AuthorForm()

    return render(request,html,{'form': form})

def login_view(request, *args, **kwargs):
    html = 'generic_form.html'

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = authenticate(username = data['username'], password=data['password'])
            if u is not None:
                login(request, u)
            else:
                return HttpResponseRedirect(reverse('login_view'))
            return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()

    return render(request,html,{'form': form})

def signup_view(request, *args, **kwargs):
    html = 'generic_form.html'

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(username=data['username'], password=data['password'])
            Author.objects.create(user=u, name=data['name'], bio=data['bio'])
            login(request, u)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()

    return render(request,html,{'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))