from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages # show messages to user


# Create your views here.
def home(request):
	# check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Auth
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been logged in!")
		else:
			messages.success(request, "There was an error")
		return redirect('home')

	return render(request, 'home.html', {
	})

#def login_user(request):
#	pass

def logout_user(request):
	logout(request)
	messages.success(request, "You have been Logged Out")
	return redirect('home')