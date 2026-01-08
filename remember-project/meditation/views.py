from django.shortcuts import render

# Create your views here.
def meditation_page(request):
    return render(request, 'meditation/meditation_page.html')