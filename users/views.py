from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from django.urls import reverse
from django.contrib import messages
# Create your views here.

class SignUpView(View):
	form_class = UserRegistrationForm
	template_name = 'auth/signup.html'


	def get(self, request):
		"""
		display register form
		"""
		form = self.form_class()
		context = {'form': form}

		return render(request, self.template_name, context)

	def post(self, request):
		"""
		handle post method
		"""
		form = self.form_class(data=request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, message="Your account was successfully created !")
			return redirect(reverse('login'))

		context = {'form': form}
		return render(request, self.template_name, context)
