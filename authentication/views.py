from django.shortcuts import render
from django.views import View

# Create your views here.

def index_auth(request):
    return render(request, 'base_auth.html')


class Sign_in_View(View):
    def get(self, request):
        return render(request, 'authentication/sign-in.html')
class Sign_up_View(View):
    def get(self, request):
        return render(request, 'authentication/sign-up.html')
class forgot_password_View(View):
    def get(self, request):
        return render(request, 'authentication/forgot_password.html')
class new_password_View(View):
    def get(self, request):
        return render(request, 'authentication/new_password.html')
