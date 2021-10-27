
from django.shortcuts import render, redirect
from .models import movie
from .forms import movieform
# Create your views here.
def index(request):
    new= movie.objects.all()
    context={
        'movie_list':new
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    new1=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':new1})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie1=movie(name=name,desc=desc,year=year,img=img,)
        movie1.save()
    return render(request,"add.html")

def update(request,id):
    movie2=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movie2)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie2})
def delete(request,id):
    if request.method=='POST':
        movie3 = movie.objects.get(id=id)
        movie3.delete()
        return redirect('/')
    return render(request,'delete.html')