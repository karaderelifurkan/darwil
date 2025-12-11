from django.shortcuts import render

from .forms import RegisterForm,LoginForm

# Create your views here.



def register(request):


    if request.method == "POST":
        form = RegisterForm(request.POST or  None)  # POST VEYA GET KONTROL  EDER
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")


            User = user(username = username)
            User.set_password(password)
            User.save()

            login(request,User)
            #messages.success(request,"Başarıyla Kayıt Oldunuz...")  #    messages.tags = succes
            return redirect("index")
        
         
        form  = RegisterForm()
        context  = { "form" : form}                
        return render(request,"register.html",context)


    form  = RegisterForm()
    context  = { "form" : form

    }
    return render(request,"register.html",context)

    
def loginUser(request):

    form = LoginForm(request.POST or None)

    context = {"form":form,}

    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        User = user(request, username = username, password = password)

        if user is None:

            messages.info(request,"Kullanıcı Adı veya Parola Hatatlı")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yapıldı")
        login(request,user)
        
        return redirect("index")
    
    return render(request,"login.html",context)






def logoutUser(request):

    logout(request)
    messages.success(request,"Başarıyla Çıkş Yaptınız")

    return redirect("index")