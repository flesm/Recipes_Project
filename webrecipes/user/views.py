from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout

from .forms import LoginUserForm, RegisterUserForm
from .models import User


class RegisterUser(CreateView):
    def get(self, request):
        return render(request, 'cooking_recipes/register.html')

    def post(self, request):
        form = RegisterUserForm(request.POST)
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        is_admin = request.POST.get("is_admin", False)
        # is_admin = request.POST["is_admin"]
        user = User.objects.create_user(username=username, email=email, password=password, is_admin=is_admin)
        form = RegisterUserForm(request.POST)

        return redirect('user:login')

    # def post(self, request):
    #     form = RegisterUserForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data["username"]
    #         email = form.cleaned_data["email"]
    #         password = form.cleaned_data["password"]
    #         is_admin = form.cleaned_data["is_admin"]
    #         user = User.objects.create_user(username=username, email=email, password=password, is_admin=is_admin)
    #         return redirect('user:login')
    #     else:
    #         return render(request, 'cooking_recipes/register.html', {'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'cooking_recipes/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('user:login')
