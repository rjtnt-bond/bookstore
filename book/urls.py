from django.contrib import admin
from django.urls import path
from book.views import home,bookstore,showbook,editbook,deletebook,StudentInfo
urlpatterns = [
    path("",home,name="homepage"),
    path("storebook/",bookstore,name="storebook"),
    path("showbook/",showbook,name="showbook"),
    path("edit_book/<int:id>",editbook,name="editbook"),
    path("delete_book/<int:id>",deletebook,name="deletebook"),
    path('studentinfo/',StudentInfo,name="StudentInfo"),
  
 
]
