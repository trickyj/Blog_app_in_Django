from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(request):
	#1) if its post request, then take the data from the user and validate it.
	if request.method =='POST':
	#we are passing in all the data into a new instance under usercreationform below.
		form = UserCreationForm(request.POST)
	#check if form is valid or invalid and save the user.
		if form.is_valid():
		# we created the user variable and save the user data in it and use this to log the user.
			user = form.save()
			login(request, user)
		

	#3) if the form is valid then we will redirect the user to page list.	
			return redirect('pages:list')
	
	#2) if the method is a get request then the below code will execute. It will take them to same signup form. This is a fresh version of the form.	
	else:
		form = UserCreationForm()
	return render(request,'accounts/signup.html',{'form': form})

def login_view(request):
	if request.method =='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log the user here
			# we retrive the user from the form and then login the user.
			user = form.get_user() 
			login(request, user)

			#After we logged the user in then lets just check if next property object exisit in the POST. and redirect is to create page
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else: 
				return redirect('pages:list')

	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('pages:list')


