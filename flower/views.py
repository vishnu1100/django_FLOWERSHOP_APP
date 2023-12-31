from django.shortcuts import render,redirect
from .models import login as log
from .models import user as usr
from .models import Products as product
from .models import staff as stafff


# Create your views here.

def index(request): 
    data=product.objects.all()
    return render(request,"index.html",{"data":data})
def contact(request): 
    return render(request,"contact.html")
def about(request): 
    return render(request,"about.html")
def shop(request): 
    return render(request,"shop.html")
def blog(request): 
    return render(request,"blog.html")
def faq(request): 
    return render(request,"faq.html")
def login(request):
    return render(request,"login.html")
def customer(request):
    return render(request,"customer.html")
def staff(request):
    return render(request,"staff.html")
def cart(request):
    return render(request,"cart.html")
def adminhome(request):
    return render(request,"adminhome.html")
def data(request):
    return render(request,"data.html")
def addproduct(request):
    return render(request,"addproduct.html")


def adminlogin(request):
    t1=request.POST.get("username")
    t2=request.POST.get("password")
    dlog=log.objects.filter(username=t1,password=t2).count()

    # _______---loop for different landing Pages--_____


    if dlog==1:
        logd=log.objects.get(username=t1,password=t2)
        if  logd.role=="admin":
            request.session["logid"]=logd.logid
            request.session["role"]=logd.role
            request.session["username"]=t1
            response=redirect('/adminhome')
            return response
        
    else:
        msg="invalid email or password"
        return render(request,"login.html",{"msg":msg})
    
   
   # _______---Customer registraion function--_____


def customerreg(request):
     fullname=request.POST["fullname"]
     address=request.POST["address"]
     mobileno=request.POST["mobileno"]
     mail=request.POST["mail"]
     username=request.POST["username"]
     password=request.POST["password"]
     
     log.objects.create(username=username,password=password,role="customer")
     data=log.objects.last()
     usr.objects.create(login=data,fullname=fullname,addr=address,mail=mail,mobileno=mobileno,status="waiting")
     response=redirect("login")
     return response 

# _______---Staff registraion function--_____



def staffreg(request):
     fullname=request.POST["fullname"]
     address=request.POST["address"]
     mobileno=request.POST["mobileno"]
     mail=request.POST["mail"]
     username=request.POST["username"]
     password=request.POST["password"]
     aadhar=request.POST["aadhar"]
     
     log.objects.create(username=username,password=password,role="staff")
     data=log.objects.last()
     stafff.objects.create(login=data,fullname=fullname,aadhar=aadhar,addr=address,mail=mail,mobileno=mobileno,status="waiting")
     response=redirect("login")
     return response 

def data(request):
     data=usr.objects.all()
     return render(request,"data.html",{"data":data})


def staffdata(request):
     data=stafff.objects.all()
     return render(request,"staffdata.html",{"data":data})



# _______---Adding Products to DB function--_____



def addproducts(request):
     pn=request.POST["pn"]
     pq=request.POST["pq"]
     pp=request.POST["pp"]
     pc=request.POST["pc"]
     pi=request.FILES["pi"]  
     product.objects.create(pn=pn,pq=pq,pp=pp,pc=pc,pi=pi)
     response=redirect("adminhome")
     return response 


def productdata(request):
     data=product.objects.all()
     return render(request,"productdata.html",{"data":data})


def pdts(request):
     data=product.objects.all()
     return render(request,"productdata.html",{"data":data})

