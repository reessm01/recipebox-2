"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from recipebox.views import index, recipeurl, authorurl, add_recipe, add_author, login_view, signup_view, logout_view, editrecipe, favorite
from recipebox.models import Recipe, Author

admin.site.register(Recipe)
admin.site.register(Author)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path('recipe/<id>', recipeurl),
    path('author/<id>', authorurl),
    path('addrecipe/', add_recipe),
    path('addauthor/', add_author),
    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view),
    path('editrecipe/<id>', editrecipe),
    path('favorite/<id>', favorite)
]
