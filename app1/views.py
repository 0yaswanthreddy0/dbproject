from django.shortcuts import render,redirect
from app1.models import Author,Book

# Create your views here.
def Home(request):
    obj=Book.objects.all()[::-1]
    return render(request,'index.html',{'books':obj})

def CreateAuthor(request):
    if request.method=="POST":
        author=request.POST.get('aname')
        age=request.POST.get('age')
        rating=request.POST.get('rating')
        obj=Author(author=author,age=age,rating=rating)
        obj.save()
        return redirect('book')
    return render(request,'author.html')

def CreateBook(request):
    if request.method=="POST":
        title=request.POST.get('bname')
        price=request.POST.get('price')
        genre=request.POST.get('genre')
        a=request.POST.get('sno')
        if Author.objects.filter(id=a).exists():
            d=Author.objects.get(id=a)
            obj=Book(title=title,price=price,genre=genre,author=d)
            obj.save()
            return redirect('homepage')
    return render(request,'book.html')

def deleteView(request):
    return render(request,'home.html')
