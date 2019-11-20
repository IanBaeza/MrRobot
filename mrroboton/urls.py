from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('inicio/',views.inicio,name='inicio'),
    path('galeria/',views.galeria,name='galeria'),
    path('pc/',views.pc,name='pc'),
    path('registro/',views.registro,name='registro')
    
]