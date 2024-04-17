from django.shortcuts import render

def index(request):
    # it,s call render templates Globally
    # nicehr line amrah aktah user requeest er thorw teh aktah template render korchi tai render function tah teh 2 tah argument deoa lagteche request and template name,index.html tah jeh folder a aceh amrah seh folder tah keh settigns.py er ai line a add koreh dichi 'DIRS': ['Templates',], karon a Templates folder tah outer project folder thats why amader ata use korteh holeh seeting.py keh aghe infrom korteh hobhe.
    return render(request, 'index.html')