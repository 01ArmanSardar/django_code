from django.shortcuts import render 
import datetime
# Create your views here.
def home (request):
    dic={'name' : 'Arman' , 'age': '24', 'list' :['python','is','too','much','good'] , 'myCountry': 'bangladesh', 'CurrentDate':datetime.datetime.now(), 'CurrentTime':datetime.datetime.now() , 'intvalue':10,'intlst':[2,4,3,5],'details':'PyThon Is GoOd FoR Opp','PlList':['Ruby','C','C++','java','Python'],
       'friends': [
           {
            'name':'kamrul',
            'age':45,
            'address':'noakhali'  
           },
           {
            'name':'habib',
            'age':49,
            'address':'noakhali'  
           },
           {
            'name':'tamim',
            'age':25,
            'address':'chandpur'  
           },
       ] }
    return render(request ,'home.html', dic)
