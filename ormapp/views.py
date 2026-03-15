from django.shortcuts import render
from .models import Employees


def home_view(request):
    all_employees = Employees.objects.all()

    context = {
        'ism': 'Fakhriddin',
        'employees': all_employees
    }
    return render(request, 'index.html', context)