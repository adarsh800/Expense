from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'e_base.html')
def dashboard(request):
    return render(request, 'expensedashboard/index_dashboard.html')
def billing(request):
    return render(request, 'expensedashboard/billing.html')
def subexpense(request):
    return render(request, 'expensedashboard/table.html')
def notifications(request):
    return render(request, 'expensedashboard/notifications.html')
def profile(request):
    return render(request, 'expensedashboard/profile.html')
