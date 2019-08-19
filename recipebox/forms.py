from django import forms
from recipebox.models import Author, Recipe
from django.forms import ModelForm

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'time_required', 'instructions', 'author']
    

# class RecipeForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     description = forms.CharField(max_length=500)
#     time_required = forms.CharField(max_length=20)
#     instructions = forms.CharField(widget=forms.Textarea)
#     author = forms.ModelChoiceField(queryset=Author.objects.all())

class AuthorForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

#     title = models.CharField(max_length=50)
#     description = models.CharField(max_length=500)
#     time_required = models.CharField(max_length=20)
#     instructions = models.TextField(blank=True, null=True)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)