from django.shortcuts import render
from app_2.models import studytable,PageVisit
from django.http import HttpResponse
from django.db.models import Q
from django.core.mail import send_mail

# Create your views here.
def myform (request):
    if request.method=="POST":
        Firstname=request.POST["name1"]
        Lastname=request.POST["name2"]
        Age=request.POST["name3"]
        Gender=request.POST["gender"]
        Email=request.POST["name4"]
        Mob=request.POST["name5"]
        Qualification=request.POST["name6"]
        Dob=request.POST["name7"]
        Username=request.POST["name8"]
        Password=request.POST["name9"]
        Image=request.FILES["name10"]
        db=studytable(Firstname=Firstname,Lastname=Lastname,Age=Age,Gender=Gender,Email=Email,Mob=Mob,Qualification=Qualification,Dob=Dob,Username=Username,Password=Password,Image=Image)
        db.save()
        return HttpResponse("data is saved")





    return render(request,"form.html")


def mydata (request):
    data=studytable.objects.all()
    return render(request, "data.html",{"datakey":data})


def delete(request,id1):
    a=studytable.objects.get(id=id1)
    a.delete()
    return HttpResponse("deleted")


def display_firstnames(request):
    firstnames = []
    if request.method == "POST":
        firstnames = studytable.objects.values_list('Firstname', flat=True)
    return render(request, 'display_firstname.html', {'firstnameskey': firstnames})


def update(request,id2):
    q = studytable.objects.get(id=id2)
    if request.method == "POST":
        q.Firstname = request.POST["name1"]
        q.Lastname = request.POST["name2"]
        q.Age = request.POST["name3"]
        q.Gender = request.POST["gender"]
        q.Email = request.POST["name4"]
        q.Mob = request.POST["name5"]
        q.Qualification = request.POST["name6"]
        q.Dob = request.POST["name7"]
        q.Username = request.POST["name8"]
        q.Password = request.POST["name9"]
        if 'change_image' in request.POST:
            q.Image = request.FILES["name10"]
        q.save()
        return HttpResponse("Update Success")

def search(request):
    if request.method=="POST":
        x=request.POST["name1"]
        y=studytable.objects.filter(Q(Firstname__icontains=x))
        if not y:
            return HttpResponse("no results found")
        return render(request,"data.html",{"searchkey":y})


    return render(request, "profile page.html", {"userprofilekey": q})

def send_email(request):
    if request.method=="POST":
        a=studytable.objects.values_list('Email',flat=True)
        for i in a :
            subject="hello"
            message="welcome to mail"
            from_email= "rahulscpo9718@gmail.com"
            receiver=[i]
            send_mail(subject,message,from_email,receiver,fail_silently=False)

        return HttpResponse("mail send success")
    return render(request,"mail.html")



def card(request):
    a=studytable.objects.all()
    return render(request,"card.html",{"keyname":a})


def productinfo(request,id3):
    a=studytable.objects.filter(id=id3).first()
    return render(request,"card_details.html",{"keydetails":a})

def home(request):
    # Get or create the PageVisit object
    page_visit, created = PageVisit.objects.get_or_create(pk=1)

    # Increment the count
    page_visit.count += 1
    page_visit.save()
    return render(request, "Home.html", {"keypagevisit": page_visit.count})