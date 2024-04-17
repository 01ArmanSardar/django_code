from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'NavigationApp/about.html')

def contact(request):
    return render(request, 'NavigationApp/contact.html')
