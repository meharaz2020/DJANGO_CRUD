from django.shortcuts import render
from django.http import HttpResponse
from first import form
from first.models import Musician,Album
from django.db.models import Avg
from django.shortcuts import redirect
# Create your views here.
def index(request):
    musician_list=Musician.objects.order_by('first_name')
    
    diction={'title':'Home Page','musician_list':musician_list}
    return render(request,'first_app/index.html',context=diction)
def album_list(request,ar_id):
    ar_info=Musician.objects.get(pk=ar_id)
    al_list=Album.objects.filter(artist=ar_id).order_by('name')
    al_list_avg=Album.objects.filter(artist=ar_id).aggregate(Avg('num_stars'))
    diction={'title':'Album Page','ar_info':ar_info,'al_list':al_list,'al_list_avg':al_list_avg}
    return render(request,'first_app/album_list.html',context=diction)

def museum_form(request):
    forms=form.MusicainForm()
    
    if request.method=='POST':
        forms=form.MusicainForm(request.POST)
        
        if forms.is_valid():
            forms.save(commit=True)
            return index(request)
            
    diction={'title':'Musician Page','museum_form':forms}
    return render(request,'first_app/musician.html',context=diction)
def album_form(request):
    forms=form.AlbumForm()
    
    if request.method=='POST':
        forms=form.AlbumForm(request.POST)
        
        if forms.is_valid():
            forms.save(commit=True)
            return index(request)
    diction={'title':'Album Form Page','AlbumForm':forms}
    return render(request,'first_app/album.html',context=diction)


def edit_ar(request,ar_id):
    ar_info=Musician.objects.get(pk=ar_id)
    forms=form.MusicainForm(instance=ar_info)
    if request.method=='POST':
         forms=form.MusicainForm(request.POST,instance=ar_info)
         
         if forms.is_valid():             
          
            forms.save(commit=True)
            return album_list(request,ar_id)

    diction={'museum_form':forms,'ar_info':ar_info}
    return render(request,'first_app/edit.html',context=diction)


def delete(request,ar_id):
    ar_info=Musician.objects.get(pk=ar_id).delete()
    if request.method=='GET':
     diction={}
    return index(request)

    # return render(request,'first_app/delete.html',context=diction) 
