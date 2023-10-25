from django.shortcuts import render,redirect
from datetime import datetime
from myapp.models import SignUp
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
logged_in = False
context_home={'current_herf':"/signup",'current':"Sign Up"}
# Create your views here.
def index(request):
    global logged_in
    if logged_in==True:
        context_home["current_herf"]= "/signout"
        context_home["current"] = "Log Out"
        messages.success(request," Logged In Succesful")
        logged_in = False
    return render(request,"index.html",context=context_home)

def about(request):
    return render(request,"About.html")
def blogs(request):
    return render(request,"blog.html")


def createuser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username) 
            messages.error(request,"User already exists")
            return redirect("/signup")
        except:
            signup = SignUp(username = username , email = email, password = password, date = datetime.today())
            signup.save()
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect("/signin")
def signup(request):
    return render(request,"SignUp.html")



def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password= password)    
        if user is not None:
            login(request,user)
            global logged_in 
            logged_in= True
            return redirect("/")

    return redirect("/signin")
        
def signin(request):
    return render(request, "SignIn.html")

def signout(request):
    global logged_in
    logged_in = False
    context_home["current_herf"]= "/signup"
    context_home["current"] = "Sign Up"
    logout(request)
    messages.success(request," Logged Out Succesful")
    return redirect("/")


def mohadi(request):
    context={
        'title':"Mohadi Falls",
        'subtitle':"It's Real water",
        'category':"Mountains",
        'mainimg':"img/mohadi-1.jpeg",
        'description':"The breathtaking sight of water falling from a height is always thrilling, and Mohadi Waterfalls are just the perfect spot where you would take your family to visit for a picnic. Easily accessible, the Waterfall is located at a distance of 30 kms from Indore, it is an idyllic picnic spot if you are looking for a break from the monotony of life and want to be with your family.",
        'img1':"img/aaaa.jpg",
    }
    return render(request,"base-info.html",context)



# context={
#         'title':"Mohadi Falls",
#         'subtitle':"It's Real water",
#         'category':"Mountains",
#         'mainimg':"img/mohadi1.jpeg",
#         'description':"The breathtaking sight of water falling from a height is always thrilling, and Mohadi Waterfalls are just the perfect spot where you would take your family to visit for a picnic. Easily accessible, the Waterfall is located at a distance of 30 kms from Indore, it is an idyllic picnic spot if you are looking for a break from the monotony of life and want to be with your family.",
#         'img1':"",
#     }