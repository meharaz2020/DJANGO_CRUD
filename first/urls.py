# from django.conf.urls import url 
from django.urls import path
from first import views 
urlpatterns=[
    path('',views.index,name='index_us'),
    path('add_album/',views.album_form,name='album_form'),
    path('add_musician/',views.museum_form,name='museum_form'),
    path('album_list/<int:ar_id>/',views.album_list,name='album_list'),
    path('edit/<int:ar_id>/',views.edit_ar,name='edit'),
    path('delete/<int:ar_id>/',views.delete,name='delete'),
    # path('',views.index,name='index'),
    # path('',views.index,name='index'),
]