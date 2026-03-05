from urllib import request

from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from .models import users

# Create your views here.
class CustomLoginView(LoginView):
    """Custom login view that redirects admins to the admin panel."""
    template_name = 'testdevtt/login.html'
    
    def get_success_url(self):
        """Redirect admins to /admin/, regular users to home."""
        if self.request.user.is_staff:
            return '/admin/'
        return '/'


def home(request):
    # display home page and handle submissions
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')
        users.objects.create(name=name, age=age, email=email, password=password)
        return redirect('view_records')
    return render(request, 'testdevtt/home.html')


def add_records(request):
    # show form and save new record
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')
        users.objects.create(name=name, age=age, email=email, password=password)
        return redirect('view_records')
    return render(request, 'testdevtt/add_records.html')


def view_records(request):
    user = users.objects.all()
    return render(request, 'testdevtt/view_records.html', {'users': user})
   