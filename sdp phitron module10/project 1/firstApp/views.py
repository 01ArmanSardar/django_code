from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # it,s call render Templates form app
    # apps tekeh kono Templates er under a takah template render korteh holeh ,settings.py a gie boleh diteh hobeh nah ,jemon akhne amrah Templates\firstApp dichi abong tar modeei template gulu rekhe dici ,apps er moddeh template use korar belai a benenfit tah paioa jai ,aladah koreh settings.py infrome korteh hoi nah  
    return render(request, 'firstApp/home.html')