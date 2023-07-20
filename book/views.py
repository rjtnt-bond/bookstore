from django.shortcuts import render,redirect
from book.forms import BookStoreFrom,StudentinfoFrom,teacherinfoForm
from book.models import BookStoreModel,Studentinfo,Teacherinfo
# Create your views here.

def home(request):
    return render(request,"homepage.html")


def bookstore(request):
    if request.method=='POST':
        # print("hello")
        book=BookStoreFrom(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('showbook')
    else:
        book=BookStoreFrom()
    return render(request,'store-book.html',{'form':book})

def showbook(request):
    bookdata=BookStoreModel.objects.all()
    return render(request,"show-book.html",{'data':bookdata})


def editbook(request,id):
    book=BookStoreModel.objects.get(pk=id)
    form=BookStoreFrom(instance=book)
    if request.method=='POST':
        # print("hello")
        book=BookStoreFrom(request.POST,instance=book)
        if book.is_valid():
            book.save()
            return redirect('showbook')
    return render(request,"store-book.html",{'form':form})

def deletebook(request,id):
    book=BookStoreModel.objects.get(pk=id).delete()
    return redirect("showbook")

def StudentInfo(request):
    if request.method=='POST':
        stuinfo=StudentinfoFrom(request.POST)
        if stuinfo.is_valid():
            stuinfo.save()
            return redirect("StudentInfo")
    else:
        stuinfo=StudentinfoFrom()
    return render(request,"Studentinfo.html",{'Studentinfo':stuinfo})
            
            
    