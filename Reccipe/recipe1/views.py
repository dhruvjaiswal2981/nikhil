import register
from django.shortcuts import render, redirect
from .models import Recepie
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, template_name='index.html')
@login_required(login_url='/login/')
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        print(recipe_name)
        print(recipe_description)
        print(recipe_image)

        Recepie.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,


        )
        return redirect('/recipes/')
        # all data store in queryset
    queryset = Recepie.objects.all()
    context = {'recipes': queryset}





    return render(request ,"recipes.html", context)

def delete_recipe(request,id):
    queryset = Recepie.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')

def update_recipe(request,id):
    queryset = Recepie.objects.get(id = id)
    context = {'recipe': queryset}

    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image
        queryset.save()
        return redirect('/recipes/')

    return render(request, "update_recipe.html", context)





def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():  # it's return boolean expresion 'exists'
            messages.info(request, 'Invalid Username')
            return redirect('/login/')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.info(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipes/')







    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')



def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Password validation
        if len(password) < 6:
            messages.info(request, "Password must be at least 6 characters long.")
            return redirect('/register/')
        if not re.search(r'\d', password):
            messages.info(request, "Password must contain at least one number.")
            return redirect('/register/')
        if not re.search(r'[A-Z]', password):
            messages.info(request, "Password must contain at least one uppercase letter.")
            return redirect('/register/')
        if not re.search(r'[a-z]', password):
            messages.info(request, "Password must contain at least one lowercase letter.")
            return redirect('/register/')
        if not re.search(r'[@$!%*?&]', password):
            messages.info(request, "Password must contain at least one special character.")
            return redirect('/register/')

        # Check if the username already exists
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')

        # Create the user
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)  # Encrypt the password
        user.save()

        return redirect('/register/')

    return render(request, 'register.html')