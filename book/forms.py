from django import forms
from book.models import BookStoreModel,Studentinfo,Teacherinfo
class BookStoreFrom(forms.ModelForm):
   class Meta:
       model=BookStoreModel
       exclude=['first_pub','last_pub']
   def __str__(self) -> str:
           return f"{self.book_name}"
       

class StudentinfoFrom(forms.ModelForm):
   class Meta:
       model=Studentinfo
       fields=['name','city','section','payment']
      
   def __str__(self) -> str:
           return f"{self.name}"
       
       
class teacherinfoForm(forms.ModelForm):
   class Meta:
       model=Teacherinfo
       fields=['name','city','department','salary']
      
   def __str__(self) -> str:
           return f"{self.name}"
       
    