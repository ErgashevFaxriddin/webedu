from django.shortcuts import render

from .models import Employees  # O'z appingizdagi modelni chaqiring


def home_view(request):
    # Bazadagi barcha xodimlarni olish
    all_employees = Employees.objects.all()

    context = {
        'ism': 'Fakhriddin',
        'employees': all_employees
    }
    return render(request, 'index.html', context)
