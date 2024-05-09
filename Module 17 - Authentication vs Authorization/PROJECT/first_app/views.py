from django.shortcuts import render ,redirect
from .forms import RegisterForm ,changeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate ,login,logout,update_session_auth_hash

# Create your views here.
def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method =='POST':
        Rform=RegisterForm(request.POST)
        if Rform.is_valid():
            messages.success(request,'account created succesfully')
            Rform.save(commit=True)
            print(Rform.cleaned_data)
    else:
        Rform=RegisterForm()
    return render(request,'signup.html',{'Rdform':Rform})

def User_login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass=form.cleaned_data['password']

                user = authenticate(username=name,password=userpass) # ai authenticate function die amrrah chek kortechi jeh user er data databas ache kinah

                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form=AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')
    
# def profile(request):
#     if request.user.is_authenticated:
#         return render(request,'profile.html',{'user':request.user})
#     else:
#         return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form=changeUserData(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'account updated succesfully')
                form.save(commit=True)
                print(form.cleaned_data)
        else:
            form=changeUserData(instance=request.user)
        return render(request,'profile.html',{'form':form})
    else :
        return redirect('signup')


def user_log_out(request):
    logout(request)
    return redirect ('login')


def pass_change(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form =PasswordChangeForm(user=request.user,data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)  #password update korbhe
                return redirect ('profile')
        else :
            form=PasswordChangeForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login')


def pass_change_withoutOLd(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form =SetPasswordForm(user=request.user,data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)  #password update korbhe
                return redirect ('profile')
        else :
            form=SetPasswordForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login')


def change_user_data(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form=changeUserData(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'account created succesfully')
                form.save(commit=True)
                print(form.cleaned_data)
        else:
            Rform=changeUserData()
        return render(request,'profile.html',{'form':form})
    else :
        return redirect('signup')