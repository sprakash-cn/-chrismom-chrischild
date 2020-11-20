from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def dashboard(request):
    return render(request, "user/dashboard.html")
