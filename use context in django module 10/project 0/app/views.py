from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    # nicher line amrah aktha dictionary create korlam abong a dictionary er maddomhe frontend a data patabhoo ar a process tah keh boleh CONTEXT
    d = {'name' : 'Arman', 'age' : '30', 'birthday' : datetime.datetime.now(), "val" : ' ' , 'value' : 30,'lst': ['python','is','best'], 'courses' : [
        {
            'id' : 1,
            'name':'python',
            'fee' : 1000,
        },
        {
            'id' : 2,
            'name':'java',
            'fee' : 10000,
        },
        {
            'id' : 8,
            'name':'django',
            'fee' : 2000,
        },

    ]}
    # uporer dictionary tah amrha cailei nicher line a d er jaigai direct declare korteh parih ,avbeh declare korleo hobhe
    return render(request, 'index.html', d)