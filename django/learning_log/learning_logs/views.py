from django.shortcuts import render

def index(request):
    """The home page for Learning Log."""
    return render(request, 'Learning_logs/index.html')

