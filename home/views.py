from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.
def signup(request): #signup Page
	if request.user.is_authenticated:
		return redirect('/home/')
	elif not request.user.is_authenticated:
		form = UserCreationForm(request.POST or None)
		#overriding max_length of form fields.
		form.fields['username'].widget.attrs['maxlength'] = '20'
		form.fields['password1'].widget.attrs['maxlength'] = '25'
		form.fields['password2'].widget.attrs['maxlength'] = '25'
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			if len(username) > 20 or len(password) > 25:
				return redirect('/signup/')
			form.save()
			new_user = authenticate(username=username, password=password)
			login(request, new_user)
			return redirect("/")
		return render(request, 'registration/signup.html', {'form': form})
		
	else:
		return redirect('signup/')

def logout(request): #Log out from the app
	from django.contrib.auth import logout
	logout(request)
	return redirect('/')
