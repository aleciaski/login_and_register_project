from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

import bcrypt
from .models import User, UserManager
# the index function is called when root is visited
def index(request):
	print("THIS IS THE INDEX!!!!!!!!!!!")
	if request== 'POST':
		return redirect('/')
	else:
		return render(request, "login_reg_app/index.html")

def success(request):
	print("THIS IS SUCCESS!!!!!!!!!!!!")
	if request.session['user_id']:
		return render(request, 'login_reg_app/success.html', {"user": User.objects.get(id=request.session['user_id'])})
	else:
		return redirect('/')
	
def register(request):
	print("REGISTER!!!!!!!")
    # to check if info is valid
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    else:
        email = request.POST['email']
        # to check if the email already exists
        try:
            User.objects.get(email=email)
            messages.error(request, "A user with this email already exists")
            return redirect('/')
        except:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
            # creating new user
            this_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password)
            request.session['user_id'] = this_user.id
            errors["success"] = "Successfully registered (or logged in)!"
            return redirect('/success')

def login(request):
    email = request.POST['email']
    # to see if it has been registered
    try:
        this_user = User.objects.get(email=email)
        if bcrypt.checkpw(request.POST['password'].encode(), this_user.password.encode()):
            request.session['user_id'] = this_user.id
            messages.error(request, "Successfully registered (or logged in)!")
            print (this_user)
            return redirect('/success')
        else:
            messages.error(request, "Incorrect password")
            return redirect('/')
    except:
        messages.error(request, "Email not found")
        return redirect('/')

def logout(request):
    request.session['user_id'] = None
    messages.error(request, "You have successfully logged out")
    return redirect('/')
	# User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
	# return render(request,"login_reg_app/success.html")


