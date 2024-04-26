from django.shortcuts import render 

# Create your views here.
def home(request):
    return render(request, 'Apphome.html')
def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select=request.POST.get('select')
        return render(request, 'About.html', {'name':name, 'email':email,'select':select})
    else:
        return render(request, 'About.html')
    
def submitfrom(request):
    return render(request, 'from.html')