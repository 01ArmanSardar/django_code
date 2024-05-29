from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.
def home(request):
   response=render(request,'home.html')
   response.set_cookie('name','rahim')
#  response.set_cookie('name','karim',max_age=10)
   response.set_cookie('name','karim',expires=datetime.utcnow()+timedelta(days=7))
   return response
def get_cookie(request):
   name=request.COOKIES.get('name')

   return render(request,'get_cookie.html',{'cookie':name})

def delete_cookie(request):
   response=render(request,'delete_cokkie.html')
   response.delete_cookie('name')
   return response

# session

def set_session(request):
   data={
      'name':'rahim',
      'age':23,
      'language':'Bangla'
   }
   print(request.session.get_session_cookie_age())
   print(request.session.get_expiry_date())
   
   request.session.update(data)
   return render(request,'home.html')


def get_session(request):
    if 'name' in request.session:
        name=request.session.get('name','Guest')
        return render(request,'get_session.html',{'name':name})
    else:
       return HttpResponse("your session has been expired please login again")
# def get_session(request):
#    name=request.session.get('name','guest')
#    age=request.session.get('age')
#    return render(request,'get_session.html',{'name':name,'age':age})

def delete_session(request):
#    del request.session['name']
   request.session.flush()
   request.session.clear_expired()
   return render (request,'delete_session.html')